from flask import Flask,render_template, request
from database import*

aplicacion = Flask(__name__)

# Crear base de datos (tabla)
#crear_tabla()


@aplicacion.route('/')
def inicio():
    variable = 530
    return render_template('inicio.html', informacion = 250)

@aplicacion.route('/registro')
def registro():
    return render_template('registro.html')

@aplicacion.route('/ingresar')
def ingresar():
    return render_template('ingreso.html')

@aplicacion.route('/respuesta', methods = ['GET','POST'])
def respuesta():
    if request.method == 'POST':
        nombre = request.form.get('Nombre')
        usuario = request.form.get('Usuario')
        clave = request.form.get('Clave')

        direccion = r'D:\STEP\PYTHON\Flask\basedatos.db'
        tabla = 'Registros'

        respuesta, _ = busqueda_parametro(direccion, tabla,'usuario', usuario)
        if respuesta == True:
            return '''
                    <p> El usuario ya existe </p>
                    <a href = "/registro"> Volvel al formulario </a>
                    '''
        else:
            datos = (nombre, usuario, clave)
            registrar(direccion, tabla, datos)
            return render_template('respuesta.html', info =  datos)


    elif request.method == 'GET':
        return registro()


@aplicacion.route('/main', methods = ['GET', 'POST'])
def main():
    direccion = r'D:\STEP\PYTHON\Flask\basedatos.db'
    tabla = 'Registros'

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        clave = request.form.get('clave')
        respuesta,data = busqueda_parametro(direccion, tabla, 'usuario', usuario)

        if respuesta == False or usuario =="":
            print(respuesta)
            return 'Por favor verifique el usuario'

        elif respuesta == True and data[0][2] == clave:
            
            direccion = r'D:\STEP\PYTHON\Flask\basedatos.db'
            tabla="Registros"
            lista = buscar_todo(direccion,tabla)
            return render_template('main.html', lista = lista)

        elif respuesta == True and data[0][2] != clave:
            return 'La clave es incorrecta, por favor verifique la informacion'
        else:
            return ingresar()

    elif request.method == 'GET':
        return ingresar()

if __name__ == '__main__':
    aplicacion.run(debug = True, port = 3000)
