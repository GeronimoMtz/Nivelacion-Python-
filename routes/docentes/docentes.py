from flask import Blueprint, request, render_template, redirect,url_for
from models import Docente
from forms import DocenteForm
from app import db

appdocente = Blueprint('appdocente',__name__,template_folder="templates")

@appdocente.route('/indexDocente')
def inicio():
    docentes = Docente.query.all()
    totalDeDocentes = Docente.query.count()
    return render_template('indexDocente.html',docentes =docentes, totalDeDocentes = totalDeDocentes)

@appdocente.route('/agregarDocente',methods=["GET","POST"])
def agregar():
    docente = Docente()
    docenteForm = DocenteForm(obj=docente)
    if request.method == "POST":
        if docenteForm.validate_on_submit():
            docenteForm.populate_obj(docente)
            db.session.add(docente)
            db.session.commit()
            return redirect(url_for('appdocente.inicio'))
    return render_template('agregarDocente.html',forma=docenteForm)

@appdocente.route('/editarDocente/<int:id>',methods=["GET","POST"])
def editar(id):
    docente = Docente.query.get_or_404(id)
    docenteForm = DocenteForm(obj=docente)
    if request.method == "POST":
        if docenteForm.validate_on_submit():
            docenteForm.populate_obj(docente)
            db.session.commit()
            return redirect(url_for('appdocente.inicio'))
    return render_template('editarDocente.html',forma=docenteForm)

@appdocente.route('/detalleDocente/<int:id>')
def detalle(id):
    docente = Docente.query.get_or_404(id)
    return render_template('detalleDocente.html',docente = docente)

@appdocente.route('/eliminarDocente/<int:id>')
def eliminar(id):
    docente= Docente.query.get_or_404(id)
    db.session.delete(docente)
    db.session.commit()
    return redirect(url_for('appdocente.inicio'))