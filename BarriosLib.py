import sqlite3

conn = sqlite3.connect('barrios.db', check_same_thread=False)
cursor = conn.cursor()


def getInfrastructuraBarrio(barrio:str) -> dict:
    '''Devuelve el estado de la insfraestructura de un barrio'''
    cursor.execute(f"SELECT Familias, Agua, Electricidad, Cloaca, Paquetes  FROM barrios WHERE Nombre = '{barrio}'")
    query = cursor.fetchone()

    infraestructura = {
        "Familias": query[0],
        "Agua": query[1],
        "Electricidad": query[2],
        "Cloaca": query[3],
        "Paquetes": query[4]
    }
    
    return infraestructura
    

def getFamilias(barrio:str) -> int:
    '''Devuelve la cantidad de familias en un barrio'''
    cursor.execute(f"""SELECT Familias FROM barrios WHERE Nombre = '{barrio}'""")
    query = cursor.fetchone()

    return query[0]


def getPaquetes(barrio) -> int:
    '''Devuelve la cantidad de paquetes de un barrio'''
    cursor.execute(f"""SELECT Paquetes FROM barrios WHERE Nombre = '{barrio}'""")
    query = cursor.fetchone()

    return query[0]



def givePaquetes(barrio:str, paquetes:int):# -> None:
    '''Añade paquetes a un barrio'''
    cursor.execute(f"UPDATE barrios SET Paquetes = {int(getPaquetes(barrio))+paquetes} WHERE Nombre = '{barrio}'")
    conn.commit()

    cursor.execute(f"""UPDATE barrios SET Proporcion_paquetes = {getPaquetes(barrio)/getFamilias(barrio)} WHERE Nombre = '{barrio}'""")
    conn.commit()



def getLeastRewardedBarrios(n:int):# -> list(list(str)):
    '''Devuelve los barrios con menor tasa paquetes/familias'''
    cursor.execute(f"""SELECT Nombre, Proporcion_paquetes FROM barrios ORDER BY Proporcion_Paquetes DESC""")
    data = cursor.fetchmany(n)
    return data



def getAllBarriosFrom(provincia:str, localidad:str):# -> list(list(str)):
    '''Devuelve todos los barrios de la provincia y localidad seleccionada'''
    cursor.execute(f"""SELECT Nombre, Familias, Paquetes FROM barrios WHERE Provincia = '{provincia}' AND Localidad = '{localidad}'""")
    return cursor.fetchall()




def getBarriosDeLocalidadProvincia(provincia:str, localidad:str):# -> list(list(str)):
    cursor.execute(f''' SELECT Familias, Paquetes FROM barrios WHERE Provincia = '{provincia}' AND Localidad = '{localidad}' ''') 
    return cursor.fetchall()

def getAllFamilasYPaquetes(provincia:str, localidad:str):# -> list(int):
    '''Devuelve la cantidad de paquetes y familias en una provincia y localidad'''
    barrios = getBarriosDeLocalidadProvincia(provincia, localidad)
    familias = int()
    paquetes = int()
    for barrio in barrios:
        familias += barrio[0]
        paquetes += barrio[1]
    return (familias, paquetes)


def getAllLocalidades():
    '''Devuelve todas las localidades'''
    cursor.execute(f"""SELECT DISTINCT Localidad FROM barrios""")
    return cursor.fetchall()

def getAllProvincias():
    '''Devuelve todas las provincias'''
    cursor.execute(f"""SELECT DISTINCT Provincia FROM barrios""")
    return cursor.fetchall()

