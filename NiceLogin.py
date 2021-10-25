import sqlite3
from time import sleep
from TimeFunctions import getDay, getTime
from NiceEncrypter import Encrypter
from random import randint

conn = sqlite3.connect('APP.db', check_same_thread=False)
cursor = conn.cursor()

# Creo la tabla de usuario
cmd = '''CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    email TEXT,
    phone TEXT,
    country TEXT,
    last_login_day DATE,
    last_login_time TIME
)'''
cursor.execute(cmd)

# Creo la tabla de los datos del encriptador
cmd = '''CREATE TABLE IF NOT EXISTS encrypterData (
    times_encrypted INTEGER,
    encryter_key TEXT
)'''
cursor.execute(cmd)	


def getEncrypterData():
    '''Getter de los datos del encrypter'''
    cmd = '''SELECT * FROM encrypterData'''
    cursor.execute(cmd)
    data = cursor.fetchone()
    return (data[1], data[0]) if data is not None else (None, None)

def setEncrypterData(key, times):
    '''Setter de los datos del encrypter'''
    cmd = f'''INSERT INTO encrypterData (times_encrypted, encryter_key) VALUES ({times}, '{key}')'''
    cursor.execute(cmd)
    conn.commit()


# Consigo la key y la cantidad de veces a encriptar
key, times = getEncrypterData() 

# Creo la instania dle encriptador
encrypter = Encrypter(key)

# Si alguno de los datos falta, Los regenera
if not all(getEncrypterData()):
    key = encrypter.regenerateKey()
    times = randint(20, 100)
    setEncrypterData(key, times)




def createUser(username, password, email, phone, country):
    '''Crea usuario'''
    cmd = f'''INSERT INTO users (username, password, email, phone, country, last_login_day, last_login_time)
    VALUES ('{username}', '{encrypter.encrypt(password, times)}', '{email}', '{phone}', '{country}', '{getDay()}', '{getTime()}')'''#
    cursor.execute(cmd)
    conn.commit()

def refreshLogin(username):
    ''''Refresca la ultima vez de inicio de sesion'''
    cmd = f'''UPDATE users SET last_login_day = '{getDay()}', last_login_time = '{getTime()}'
    WHERE username = '{username}' '''
    cursor.execute(cmd)
    conn.commit()

def validateUser(username):
    '''Verifica la existencia del usuario'''
    cmd = f'''SELECT * FROM users WHERE username = '{username}' '''
    cursor.execute(cmd)
    user = cursor.fetchone()
    return user if user is None else True

def validateEmail(email):
    '''Verifica la existencia del email'''
    cmd = f'''SELECT * FROM users WHERE email = '{email}' '''
    cursor.execute(cmd)
    user = cursor.fetchone()
    return user if user is None else True

def getEmail(username):
    '''Consigue el main con el usuario'''
    user = validateUser(username)
    if user is not None:
        cmd = f'''SELECT email FROM users WHERE username = '{username}' '''
        cursor.execute(cmd)
        email = cursor.fetchone()
        return email[0]
    else:
        return None

def getUserData(username):
    '''Devuelve los datos del usuario'''
    cmd = f'''SELECT * FROM users WHERE username = '{username}' '''
    cursor.execute(cmd)
    data = cursor.fetchone()
    return data if data is not None else None

def validateLogin(username, password):
    '''Verifica el usuario y contraseña'''
    cmd = f'''SELECT * FROM users WHERE username = '{username}' AND password = '{encrypter.encrypt(password, times)}' '''
    cursor.execute(cmd)
    user = cursor.fetchone()
    return True if user is not None else False

def changePassword(username, password):
    '''Cambia la contraseña'''
    cmd = f'''UPDATE users SET password = '{encrypter.encrypt(password, times)}' WHERE username = '{username}' '''
    cursor.execute(cmd)
    conn.commit()

def changeEmail(username, email):
    '''Cambia el email'''
    cmd = f'''UPDATE users SET email = '{email}' WHERE username = '{username}' '''
    cursor.execute(cmd)
    conn.commit()

def changePhone(username, phone):
    '''Cambia el telefono'''
    cmd = f'''UPDATE users SET phone = '{phone}' WHERE username = '{username}' '''
    cursor.execute(cmd)
    conn.commit()

def updateData(username, password, email, phone, country):
    '''Actualiza los datos del usuario'''
    cmd = f'''UPDATE users SET password = '{password}', email = '{email}', phone = '{phone}', country = '{country}' WHERE username = '{username}'''
    cursor.execute(cmd)
    conn.commit()

def getUserDict(username):
    '''Devuelve los datos del usuario'''
    cmd = f'''SELECT * FROM users WHERE username = '{username}' '''
    cursor.execute(cmd)
    data = cursor.fetchone()

    return data if data is not None else None