from flask import Blueprint, request,jsonify
from models import Subway
from app import db

appsubways= Blueprint('appsubways',__name__,template_folder="templates")

@appsubways.route('/subway/agregar',methods={'POST'})
def agregaSubway():
    try:
        json = request.get_json()
        subway = Subway()
        subway.nombre = json['nombre']
        subway.ingredientes = json['ingredientes']
        subway.pan = json['pan']
        subway.precio = json['precio']
        db.session.add(subway)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"subway agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appsubways.route('/subway/editar',methods={"POST"})
def editaSubway():
    try:
        json = request.get_json()
        subway = Subway.query.get_or_404(json['id'])
        subway.nombre = json['nombre']
        subway.ingredientes = json['ingredientes']
        subway.pan = json['pan']
        subway.precio = json['precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"subway modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appsubways.route('/subway/eliminar',methods={"POST"})
def eliminaSubway():
    try:
        json = request.get_json()
        subway = Subway.query.get_or_404(json['id'])
        db.session.delete(subway)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"subway eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appsubways.route('/subway/obtener',methods={"GET"})
def obtenerSubway():
    subway = Subway.query.all()
    listaSubways=[]
    for p in subway:
        subway = {}
        subway['nombre'] = p.nombre
        subway['ingredientes'] = p.ingredientes
        subway['pan'] = p.pan
        subway['precio'] = p.precio
        listaSubways.append(subway)
    return jsonify({'subway':listaSubways})