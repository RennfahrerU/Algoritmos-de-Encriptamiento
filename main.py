import sustitucion
import transposicion
import util
import RSA

def main():
    mensaje = util.pedirmsj("Ingrese el mensaje a operar: ")
    print(f'Mensaje original: {mensaje}')

    # Test sustitución
    pos = 8
    susti_des = sustitucion_cifrar(mensaje, pos)
    sustitucion_descifrar(susti_des, pos)

    # Test Transposición
    clave = 5
    transp_descifrar = transposicion_cifrar(mensaje, clave)
    transposicion_descifrar(transp_descifrar, clave)

    # Test RSA
    
    bits = 32  # Longitud de las claves en bits
    e, d, n = RSA.gen_keys(bits) # Generar claves
    mensaje_cifrado = RSA_cifrar(mensaje, e, n)
    RSA_descifrar(mensaje_cifrado, d, n)

def sustitucion_cifrar(mensaje, pos): # Cifrar Sustitución
    cifrado = sustitucion.convertiraNumero(mensaje)
    cifrado = sustitucion.cifrar(cifrado, pos)
    mensajecifrado = sustitucion.convertiraLetra(cifrado)
    util.printResultado("cifrado",mensajecifrado)
    return mensajecifrado

def sustitucion_descifrar(mensaje_cifrado, pos): # Descifrar por Sustitución
    mensaje_cifrado = sustitucion.convertiraNumero(mensaje_cifrado)
    descifrado = sustitucion.descifrar(mensaje_cifrado, pos)
    mensajedescifrado = sustitucion.convertiraLetra(descifrado)
    util.printResultado("descifrado",mensajedescifrado)
    return mensajedescifrado

def transposicion_cifrar(mensaje, clave):
    cifrado = transposicion.cifrar(mensaje, clave)
    util.printResultado("cifrado",cifrado)
    return cifrado

def transposicion_descifrar(mensaje, clave):
    descifrado = transposicion.descifrar(mensaje, clave)
    util.printResultado("descifrado",descifrado)

def RSA_cifrar(mensaje, e, n):
    # Cifrar un mensaje
    mensaje_cifrado = RSA.encrypt(mensaje, e, n)
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    return mensaje_cifrado

def RSA_descifrar(mensaje_cifrado, d, n):
    # Descifrar el mensaje
    mensaje_descifrado = RSA.decrypt(mensaje_cifrado, d, n)
    if mensaje_descifrado is not None:
        print(f"Mensaje descifrado: {mensaje_descifrado}")
    else:
        print("Error al descifrar el mensaje.") 

if __name__ == '__main__':
    main()