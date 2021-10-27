from flask import Flask, render_template, request, make_response, session, flash, g, redirect, url_for
from flask_wtf import CSRFProtect
from werkzeug.exceptions import PreconditionRequired
from werkzeug.user_agent import UserAgent
from werkzeug.security import generate_password_hash, check_password_hash
import forms
from BarriosLib import getAllBarriosFrom, getAllFamilasYPaquetes, getLeastRewardedBarrios, givePaquetes, getInfrastructuraBarrio, getAllLocalidades, getAllProvincias, getAllBarrios
from NiceLogin import * 


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'my_secret_key'

#@app.before_request
# def before_request():
#     '''Al entrar a cualquier pagina a excepción de sign-in, si no se esta logeado se redirije a la pagina de login '''

#     if 'username' not in session and request.endpoint != 'login' or request.endpoint != 'sign-in' or request.endpoint != '/':
#         return redirect(url_for('login'))



@app.route("/")
def index():
    '''Ruta index de la pagina. Muestra un menu para dirijirse a la ruta de registro o logeo'''
    return render_template('home.html')


@app.route("/barrios", methods = ['GET', 'POST'])
def barrio():
    '''Ruta en la que se muestran todos los barrios de la provincia y localidad a ingresar. 
    Posee un hipervinculo para ir a la información mas detallada de cada barrio'''
    
    local_barrios = getAllBarrios()
    barrios = forms.BarriosForm(request.form)

    if request.method == "POST" and barrios.validate():
        
        provincia = barrios.provincia.data
        localidad = barrios.localidad.data

        session['provincia'] = provincia
        session['localidad'] = localidad
        local_barrios = getAllBarriosFrom(provincia, localidad)


    return render_template('barrios.html', form = barrios, barrios = local_barrios)

@app.route("/barrios/<barrio>", methods = ['GET', 'POST'])
def barrio_especifico(barrio):
    '''Ruta que se ingresa mediante el hipervinculo al mostrarse los barrios, muestra las condiciones de conexiones de agua,
    luz y cloacas, además de los paquetes recibidos.'''

    paquetes = ''
    paquete = forms.Packages(request.form)
    infra = getInfrastructuraBarrio(barrio)

    if request.method == "POST" and paquete.validate():
        paquetes = paquete.paquetes.data

        givePaquetes(barrio, paquetes)


    return render_template('update.html', barrio = barrio, infra = infra, paquetes = paquete)



@app.route("/estadistica", methods = ['GET', 'POST'])
def estadistica():
    '''Ruta con dos menus en la que se listan una estadística con sumatoria de familias y paquetes recibidos, por localidad y por provincia
    y los barrios con menor proporción de paquetes recibidos por familia.'''

    least_rewarded = []
    menos = forms.LeastRewarded(request.form)

    if True:#request.method == "POST":# and menos.validate():
        
        cantidad = menos.cantidad.data
        least_rewarded = getLeastRewardedBarrios(3)
    # TExtBox para mostrar n cantidad de los peores barrios hechoi, solo falta motrarlo, por ahora está hardcodeado en 3    

    data = list()
    provincias = getAllProvincias()

    for provincia in provincias:

        localidades = getAllLocalidades(provincia[0])
        familias = 0
        paquetes = 0
        
        for localidad in localidades:
            v1, v2 = getAllFamilasYPaquetes(provincia, localidad)
            familias += v1
            paquetes += v2

        data.append((provincia, localidad, familias, paquetes))


    return render_template('stats.html', provincia = session['provincia'], localidad = ['localidad'], least_rewarded = least_rewarded, data=data) 


@app.route("/login", methods = ['GET', 'POST'])
def login():
    '''Ruta para logearse'''
    login = forms.LoginForm(request.form)

    if request.method == 'POST' and login.validate():
        username = login.username.data
        passw = login.passw.data

        if validateLogin(username, passw):
            user = getUserData(username)
            session['username'] = username
            session['passw'] = user[1]
            session['email'] = user[2]

            return redirect(url_for("barrio"))

        
    return render_template('login.html', form = login)


@app.route("/logout")
def logout():
    '''Ruta para desconecta tu usuario''' 
    if "username" in session:
        flash('Te has desconectado {}'.format(session['username']))

    session.pop("username", None)
    session.pop("passw", None)
    session.pop("email", None)

    return redirect(url_for("login"))


@app.route("/sign-in", methods = ['GET', 'POST'])
def sign_in():
    '''Ruta para registrar tu usuario con la necesidad de un usuario, contraseña y email'''   
    usernamea = ''
    passw = ''
    email = ''
    sign_in = forms.Sign_In(request.form)

    if request.method == "POST" and sign_in.validate():

        usernamea = sign_in.username.data
        passw = sign_in.passw.data
        email = sign_in.email.data

        if validateUser(usernamea):
            flash("Este usuario ya esta creado")
            
        else:
            createUser(usernamea, passw, email, 'n/a', 'n/a')

    return render_template('register.html', form = sign_in)


if __name__ == '__main__':
    app.run(debug = True)


#home: hpv login register

#barrios : barra de busqueda: y l

#estads los barrios deistica: ultimas 2 conss a textoa igdato