from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField
from wtforms import validators


class UsersForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese nombre valido')
    ])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese apellido valido')
    ])
    amaterno=StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese apellido valido')
    ])

    edad=IntegerField('edad',[        
        validators.number_range(min=1, max=20,message='ingrese edad valida')
    ])
    correo=StringField('correo',[
        validators.DataRequired(message='el campo es requerido'),
    ])


    # nombre=StringField('nombre')
    # apaterno=StringField('apaterno')
    # amaterno=StringField('amaterno')
    # edad=IntegerField('edad')
    # correo=EmailField('correo')

class UsersForm2(Form):
    id=IntegerField('id')

    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese nombre valido')
    ])
    apaterno=StringField('apaterno')

    email=StringField('correo',[
        validators.DataRequired(message='ingresar un correo valido'),
    ])