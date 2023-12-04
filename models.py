from app import db

class Docente(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    edad = db.Column(db.String(255))
    carrera = db.Column(db.String(255))

class Papita(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    gr = db.Column(db.String(255))
    cantidad = db.Column(db.String(255))

class Agua(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    ml = db.Column(db.String(255))
    precio = db.Column(db.String(255))

class Subway(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    ingredientes = db.Column(db.String(255))
    pan = db.Column(db.String(255)) #TIPO DE PAN
    precio = db.Column(db.String(255))

class Pizza(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    ingredientes = db.Column(db.String(255))
    tamaño = db.Column(db.String(255))
    precio = db.Column(db.String(255))