from flask import Blueprint, request,jsonify
from models import Papita
from app import db

apppapitas= Blueprint('apppapitas',__name__,template_folder="templates")

@apppapitas.route('/papita/agregar',methods={'POST'})
def agregaPapita():
    try:
        json = request.get_json()
        papita = Papita()
        papita.nombre = json['nombre']
        papita.marca = json['marca']
        papita.gr = json['gr']
        papita.cantidad = json['cantidad']
        db.session.add(papita)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Papita agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@apppapitas.route('/papita/editar',methods={"POST"})
def editaPapita():
    try:
        json = request.get_json()
        papita = Papita.query.get_or_404(json['id'])
        papita.nombre = json['nombre']
        papita.marca = json['marca']
        papita.gr = json['gr']
        papita.cantidad = json['cantidad']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Papita modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@apppapitas.route('/papita/eliminar',methods={"POST"})
def eliminaPapita():
    try:
        json = request.get_json()
        papita = Papita.query.get_or_404(json['id'])
        db.session.delete(papita)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Papita eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@apppapitas.route('/papita/obtener',methods={"GET"})
def obtenerPapita():
    papita = Papita.query.all()
    listaPapitas=[]
    for p in papita:
        papita = {}
        papita['nombre'] = p.nombre
        papita['marca'] = p.marca
        papita['gr'] = p.gr
        papita['cantidad'] = p.cantidad
        listaPapitas.append(papita)
    return jsonify({'papita':listaPapitas})