from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'quierencoca'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['POST', 'GET'])
def login():
    print('estoy en la funcion login')
    # si el metodo es post 
    if request.method == 'POST':
        # recibimos el email en la variable emailform
        emailForm = request.form["email"]
        print(emailForm)
        # password = request.form["password"]
        # buscamos el usuario con un query y filtramos el primero
        user = User.query.filter_by(email=emailForm).first()
        print(user)
        # si el usuario existe 
        if user:
            # nos logueamos con el usuario y retornamos me loguee
            print('encontre el user')
            login_user(user)
            # return redirect(url_for('aportes'))
            # ----------cambiar por la redireccion del usuario logueado -------------------------------
            return 'ME LOGUEE'
        # ------------------------------------------------------------
        return "Holi"
    else:
        return render_template('web_login.html')


@app.route('/materiales')
def materiales():
    return render_template('materiales.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        emailNuevo = request.form['email']
        passwordNuevo = request.form['password']
        new_user = User(email=emailNuevo, password=passwordNuevo)
        db.session.add(new_user)
        db.session.commit()
        return "Cree"
    else:
        return render_template('web_register.html')


@app.route('/vistas')
def vistas_1():
    return render_template('vistas_1.html')


@app.route('/aportes')
def aportes():
    return render_template('Mis_aportes.html')


if __name__ == '__main__':
    print('corri la puta madre')
    app.run(debug=True)