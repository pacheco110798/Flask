import sqlite3

def crear_tabla():
    conexion = sqlite3.connect(r'D:\STEP\PYTHON\Flask\basedatos.db')
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE Registros (nombre VARCHAR(30), usuario VARCHAR(30) PRIMARY KEY, clave VARCHAR(30))')
    conexion.close()


def registrar(direccion, tabla, informacion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO {tabla} VALUES('{informacion[0]}','{informacion[1]}', '{informacion[2]}')")
    conexion.commit()
    conexion.close()


def busqueda_parametro(direccion, tabla, parametro, valor):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    cursor.execute(f"SELECT*FROM {tabla} WHERE {parametro} = '{valor}'")
    data = cursor.fetchall()
    conexion.close()

    # verifico si se encontro algun registro con los parametros de busqueda
    if len(data) > 0:
        return (True, data)
    else:
        return (False, data)

def buscar_todo(direccion,tabla):
    conexion =sqlite3.connect(direccion)
    cursor=conexion.cursor()
    cursor.execute(f"SELECT*FROM {tabla}")
    data=cursor.fetchall()
    print(data)
    conexion.close()
    return data