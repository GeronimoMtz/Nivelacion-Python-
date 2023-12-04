from flask import Blueprint, request,jsonify
from models import Agua
from app import db

appaguas= Blueprint('appaguas',__name__,template_folder="templates")

@appaguas.route('/agua/agregar',methods={'POST'})
def agregaAgua():
    try:
        json = request.get_json()
        agua = Agua()
        agua.nombre = json['nombre']
        agua.marca = json['marca']
        agua.ml = json['ml']
        agua.precio = json['precio']
        db.session.add(agua)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Agua agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appaguas.route('/agua/editar',methods={"POST"})
def editaAgua():
    try:
        json = request.get_json()
        agua = Agua.query.get_or_404(json['id'])
        agua.nombre = json['nombre']
        agua.marca = json['marca']
        agua.ml = json['ml']
        agua.precio = json['precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Agua modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appaguas.route('/agua/eliminar',methods={"POST"})
def eliminaAgua():
    try:
        json = request.get_json()
        agua = Agua.query.get_or_404(json['id'])
        db.session.delete(agua)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Agua eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appaguas.route('/agua/obtener',methods={"GET"})
def obtenerAgua():
    agua = Agua.query.all()
    listaAguas=[]
    for p in agua:
        agua = {}
        agua['nombre'] = p.nombre
        agua['marca'] = p.marca
        agua['ml'] = p.ml
        agua['precio'] = p.precio
        listaAguas.append(agua)
    return jsonify({'agua':listaAguas})