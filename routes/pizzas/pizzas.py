from flask import Blueprint, request,jsonify
from models import Pizza
from app import db

apppizzas= Blueprint('apppizzas',__name__,template_folder="templates")

@apppizzas.route('/pizza/agregar',methods={'POST'})
def agregaPizza():
    try:
        json = request.get_json()
        pizza = Pizza()
        pizza.nombre = json['nombre']
        pizza.ingredientes = json['ingredientes']
        pizza.tamaño = json['tamaño']
        pizza.precio = json['precio']
        db.session.add(pizza)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"pizza agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@apppizzas.route('/pizza/editar',methods={"POST"})
def editaPizza():
    try:
        json = request.get_json()
        pizza = Pizza.query.get_or_404(json['id'])
        pizza.nombre = json['nombre']
        pizza.ingredientes = json['ingredientes']
        pizza.tamaño = json['tamaño']
        pizza.precio = json['precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"pizza modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@apppizzas.route('/pizza/eliminar',methods={"POST"})
def eliminaPizza():
    try:
        json = request.get_json()
        pizza = Pizza.query.get_or_404(json['id'])
        db.session.delete(pizza)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"pizza eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@apppizzas.route('/pizza/obtener',methods={"GET"})
def obtenerPizza():
    pizza = Pizza.query.all()
    listaPizzas=[]
    for p in pizza:
        pizza = {}
        pizza['nombre'] = p.nombre
        pizza['ingredientes'] = p.ingredientes
        pizza['tamaño'] = p.tamaño
        pizza['precio'] = p.precio
        listaPizzas.append(pizza)
    return jsonify({'pizza':listaPizzas})