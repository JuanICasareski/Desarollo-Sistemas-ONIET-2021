from wtforms import Form
from wtforms import StringField, TextField, PasswordField, IntegerField
from wtforms import validators
from wtforms.fields.html5 import EmailField
class BarriosForm(Form):
    provincia = StringField('Provincia: ', [validators.required(message = "Debe ingresar una provincia")])

    localidad = StringField('Localidad: ', [validators.required(message="Debe ingresar una localidad en especifico" )])


class LoginForm(Form):
    username = StringField('Username', [validators.length(min=4, max=30, message='Ingrese un username mas largo o mas corto' ), 
                                        validators.required(message = "El username es requerido")])

    passw = PasswordField('Contraseña',[validators.required(message= 'Se necesita una contraseña')])

class Sign_In(Form):
    username = StringField('Username', [validators.length(min=4, max=30, message='Ingrese un username mas largo o mas corto' ), 
                                        validators.required(message = "El username es requerido")])

    passw = PasswordField('Contraseña',[validators.required(message= 'Se necesita una contraseña')])

    email = EmailField('Email', [validators.email(message='Ingresa un email valido'),
                                validators.required(message= 'Se necesita ingresa un email')])

class Packages(Form):
    paquetes = IntegerField('Paquetes a entregar', [validators.required(message= 'Se necesita una cantidad de paquetes a asignar')])

class LeastRewarded(Form):
    cantidad = IntegerField('Cantidad de barrios menos recompensados a entregar', [validators.required(message= 'Se necesita una cantidad')])