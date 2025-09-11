from flask import Flask, render_template, request, session
import sustitucion
import transposicion
import RSA
import ast

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_algoritmos_de_encriptacion'  # Cambia esto por una clave secura

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    mensaje_info = None
    
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
            if operacion == 'cifrar':
                resultado, mensaje_info = RSA_cifrar(mensaje)
            else:
                resultado = RSA_descifrar(mensaje)
                
    return render_template('index.html', resultado=resultado, mensaje_info=mensaje_info)

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

def RSA_cifrar(mensaje):
    bits = 32
    e, d, n = RSA.gen_keys(bits)
    # Guardar las claves en la sesión
    session['rsa_e'] = e
    session['rsa_d'] = d
    session['rsa_n'] = n
    
    mensaje_cifrado = RSA.encrypt(mensaje, e, n)
    # Convertir la lista a string para mostrar
    mensaje_cifrado_str = str(mensaje_cifrado)
    
    # Información adicional para el usuario
    info = f"Claves generadas - e: {e}, d: {d}, n: {n}. Para descifrar, usa esta lista exacta: {mensaje_cifrado_str}"
    
    return mensaje_cifrado_str, info

def RSA_descifrar(mensaje_cifrado_str):
    try:
        # Obtener las claves de la sesión
        if 'rsa_d' not in session or 'rsa_n' not in session:
            return "Error: No hay claves RSA en la sesión. Primero debes cifrar un mensaje para generar las claves."
        
        d = session['rsa_d']
        n = session['rsa_n']
        
        # Convertir el string de vuelta a lista
        try:
            mensaje_cifrado = ast.literal_eval(mensaje_cifrado_str)
        except (ValueError, SyntaxError):
            return "Error: El formato del mensaje cifrado no es válido. Debe ser una lista de números como [123, 456, 789]."
        
        if not isinstance(mensaje_cifrado, list):
            return "Error: El mensaje cifrado debe ser una lista de números."
        
        mensaje_descifrado = RSA.decrypt(mensaje_cifrado, d, n)
        return mensaje_descifrado
        
    except Exception as e:
        return f"Error al descifrar: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
