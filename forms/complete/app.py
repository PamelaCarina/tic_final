from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#TABLAS

class Clientes(db.Model):
     rut = db.Column(db.Integer, primary_key=True)
     #cv = db.Column(db.String(1), primary_key=True)
     nombre = db.Column(db.String(50), nullable=False)
     telefono = db.Column(db.Integer, unique = True, nullable = False)
     cant_libros = db.Column(db.Integer, nullable = False)
     socio = db.Column(db.Boolean, unique = True, nullable = False)

class Repisas(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), unique = True, nullable = False)


#RUTAS PARA AÑADIR O CONSULTAR COSAS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signuprep", methods=["GET","POST"]) #Ingresa repisas (lo hace el/la empleadx)
def signuprep():
    if request.method == "POST":

        nueva_repisa = Repisas(categoria = request.form["categoria"])
        db.session.add(nueva_repisa)
        db.session.commit()

        return "Tu repisa se registró de manera correcta! :D"

    return render_template("signuprep.html")

# @app.route("/signupcliente", methods=["GET","POST"]) #Registro de Clientes
# def signupcliente():
#     if request.method == "POST":
#
#         nuevx_cliente = Clientes(rut = request.form["rut"], nombre = request.form["nombre"], telefono = request.form["telefono"],
#                                  cant_libros = request.form["cant_libros"], socio = request.form["socio"])
#         db.session.add(nuevx_cliente)
#         db.session.commit()
#
#         return "Tu repisa se registró de manera correcta! :D"
#
#     return render_template("signupcliente.html")

# @app.route("/agrega_libro", methods=["GET","POST"]) #Agregar un libro al cliente
# def agrega_libro():
#     if request.method == "POST":
#
#         nuevx_cliente = Clientes(rut = request.form["rut"], nombre = request.form["nombre"], telefono = request.form["telefono"],
#                                  cant_libros = request.form["cant_libros"], socio = request.form["socio"])
#         db.session.add(nuevx_cliente)
#         db.session.commit()
#
#         return "Tu repisa se registró de manera correcta! :D"
#
#     return render_template("signupcliente.html")

# @app.route("/logincliente", method=["GET, POST"]) #El cliente puede ver su estado de libros (cuantos libros tiene a su pedido)
#  def logincliente():
#      if request.method == "POST":
#          cliente = Clientes.query.filter_by(nombre=request.form["nombre"]).first()
#
#          if cliente and Clientes.query.filter_by(rut=request.form["rut"]):
#              return "Esta es tu pulenta cuenta jjj"
#
#         return "no hrmno no coiside"

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
