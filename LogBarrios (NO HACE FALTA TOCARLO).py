import requests
import json
import sqlite3

conn = sqlite3.connect('barrios.db')
cursor = conn.cursor()

cmd = """CREATE TABLE IF NOT EXISTS barrios (
        id INTEGER PRIMARY KEY, 
        Familias estimadas INTEGER, 
        Provincia Barrio TEXT, 
        Localidad Barrio TEXT,
        Nombre Barrio TEXT, 
        Agua INTEGER, 
        Electricidad INTEGER, 
        Cloaca INTEGER,
        Paquetes INTEGER,
        Proporcion_paquetes FLOAT
        )"""
cursor.execute(cmd)


url = "https://datosabiertos.desarrollosocial.gob.ar/dataset/0d022767-9390-486a-bff4-ba53b85d730e/resource/97cc7d10-ad4c-46cb-9ee4-becb402adf9f/download/renabap-2020-11-20.geojson"

def rawString(string):
    output = ''
    for l in string:
        if l.isalpha() or l.isdigit() or l==' ':
            output += l
    return output

def getBarrios():

    barrios = requests.get(url).json()["features"]
    data = []

    for barrio in barrios:
        barrio = barrio["properties"]
        dict = {
            'Familias estimadas': barrio["Familias estimadas"],
            'Provincia Barrio': rawString(barrio["Provincia"]),
            'Localidad Barrio': rawString(barrio["Localidad"]),
            'Nombre Barrio': rawString(barrio["Barrio"]),
            'Agua': rawString(barrio['Agua']),
            'Electricidad': rawString(barrio['Electricidad']),
            'Cloaca': rawString(barrio['Cloaca'])
        }

        data.append(dict)
    return data


def logBarrios():
    data = getBarrios()
    for barrio in data:
        #print(barrio)
        cmd = f'''INSERT INTO barrios (Familias, Provincia, Localidad, Nombre, Agua, Electricidad, Cloaca, Paquetes, Proporcion_paquetes) VALUES
        ('{barrio["Familias estimadas"]}', '{barrio["Provincia Barrio"]}', '{barrio["Localidad Barrio"]}', '{barrio["Nombre Barrio"]}', '{barrio["Agua"]}', '{barrio["Electricidad"]}', '{barrio["Cloaca"]}', 0, 0)'''
        cursor.execute(cmd)
    conn.commit()
    conn.close()


logBarrios()