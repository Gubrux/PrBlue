import firebase_admin
from firebase_admin import credentials, storage, firestore
from flask import Flask, request, render_template, redirect
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker



# Configurar Firebase
cred = credentials.Certificate(r"C:\Users\kathu\Desktop\HACKATON\credenciales.json")
firebase_admin.initialize_app(cred, {
    "storageBucket": "educared-7d7c2.appspot.com"
})

bucket = storage.bucket()

# Crear la aplicación Flask
app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
        return render_template('web_login.html')    #CAMBIAAAAR

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'nuncasabrannada'
db = SQLAlchemy(app)


@app.route('/inicio')
def materiales():
    return render_template('materiales.html')

@app.route('/materiales')
def materiales():
    return render_template('inicio.html')


#modelo
# Base = declarative_base()

# crear las tablas
class FirebaseFile(db.Model):
    __tablename__ = 'firebase_files'

    id = Column(Integer, primary_key=True)
    # name = Column(String)
    url = Column(String)
    # bucket = Column(String)

    def __init__(self, url):
        # self.name = name
        self.url = url
        # self.bucket = bucket

# Definir la ruta de la página principal
@app.route("/aportes", methods=["GET"])
def index():

    lista_de_urls = db.session.query(FirebaseFile).all()

    print(lista_de_urls)

    return render_template("Mis_aportes.html", lista_de_urls=lista_de_urls)

# Definir la ruta para cargar el archivo
@app.route("/aportes", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Obtener el archivo seleccionado por el usuario
        file = request.files["test"]


        # Crear una referencia al archivo en Firebase Storage
        blob = bucket.blob("files/" + file.filename)

        # Cargar el archivo en Firebase Storage
        blob.upload_from_file(file, content_type=file.content_type)

        # Obtener la URL del archivo cargado
        blob.make_public()
        url = blob.public_url

        nuevo_url = FirebaseFile(url=url)
        db.session.add(nuevo_url)
        db.session.commit()

        lista_de_urls = db.session.query(FirebaseFile).all()
        return render_template("mis_aportes2.html", url=url, lista_de_urls=lista_de_urls)   #CAMBIAAAAR
    
with app.app_context():
    db.create_all()





@app.route('/vistas')
def vistas_1():
    return render_template('vistas_1.html')    #CAMBIAAAAR


@app.route('/aportes')
def aportes():
    return render_template('Mis_aportes.html')


if __name__ == '__main__':
    print('funcionó')
    app.run(debug=True)