from flask import Flask, render_template # request


# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # db = SQLAlchemy(app)


@app.route('/login')
def login():
    return render_template('web_login.html')


@app.route('/materiales')
def materiales():
    return render_template('materiales.html')


@app.route('/register')
def register():
    return render_template('web_register.html')


@app.route('/vistas')
def vistas_1():
  return render_template('vistas_1.html')


@app.route('/aportes')
def aportes():
  return render_template('Mis_aportes.html')


if __name__ == '__main__':
    app.run(debug=True)
