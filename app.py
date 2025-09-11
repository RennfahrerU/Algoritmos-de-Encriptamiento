from flask import Flask, render_template, request
import sustitucion
import transposicion
import util
import RSA

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        operacion = request.form['operacion']
        tipo_cifrado = request.form['tipo_cifrado']

        if tipo_cifrado == 'sustitucion':
            pos = 8
            if operacion == 'cifrar':
                resultado = sustitucion_cifrar(mensaje, pos)
            else:
                resultado = sustitucion_descifrar(mensaje, pos)
        elif tipo_cifrado == 'transposicion':
            clave = 5
            if operacion == 'cifrar':
                resultado = transposicion_cifrar(mensaje, clave)
            else:
                resultado = transposicion_descifrar(mensaje, clave)
        elif tipo_cifrado == 'RSA':
            bits = 32
            e, d, n = RSA.gen_keys(bits)
            if operacion == 'cifrar':
                resultado = RSA_cifrar(mensaje, e, n)
            else:
                resultado = RSA_descifrar(mensaje, d, n)
    return render_template('index.html', resultado=resultado)

def sustitucion_cifrar(mensaje, pos):
    cifrado = sustitucion.convertiraNumero(mensaje)
    cifrado = sustitucion.cifrar(cifrado, pos)
    mensajecifrado = sustitucion.convertiraLetra(cifrado)
    return mensajecifrado

def sustitucion_descifrar(mensaje_cifrado, pos):
    numeros = sustitucion.convertiraNumero(mensaje_cifrado)
    descifrado = sustitucion.descifrar(numeros, pos)
    mensajedescifrado = sustitucion.convertiraLetra(descifrado)
    return mensajedescifrado

def transposicion_cifrar(mensaje, clave):
    cifrado = transposicion.cifrar(mensaje, clave)
    return cifrado

def transposicion_descifrar(mensaje, clave):
    descifrado = transposicion.descifrar(mensaje, clave)
    return descifrado

def RSA_cifrar(mensaje, e, n):
    mensaje_cifrado = RSA.encrypt(mensaje, e, n)
    return mensaje_cifrado

def RSA_descifrar(mensaje_cifrado, d, n):
    mensaje_descifrado = RSA.decrypt(mensaje_cifrado, d, n)
    return mensaje_descifrado

if __name__ == '__main__':
    app.run(debug=True)
