from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DocenteForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    apellido = StringField('apellido',validators=[DataRequired()])
    edad = StringField('edad',validators=[DataRequired()]) 
    carrera = StringField('carrera',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')