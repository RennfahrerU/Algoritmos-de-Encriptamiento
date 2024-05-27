import sustitucion
import transposicion
import util

def main():
    mensaje = util.pedirmsj("Ingrese el mensaje a operar: ")
    
def test():
    susti_cifrar = "HOLA COMO ESTA"
    susti_des = "OWSI KWTW MABI"
    pos = 8
    sustitucion_cifrar(susti_cifrar, pos)
    sustitucion_descifrar(susti_des, pos)

    transp_cifrar = "HOLA COMO ESTA"
    transp_descifrar = "HOTO MALO *AE*CS*"
    clave = 5
    transposicion_cifrar(transp_cifrar, clave)
    transposicion_descifrar(transp_descifrar, clave)

def sustitucion_cifrar(mensaje, pos): # Cifrar Sustitución
    cifrado = sustitucion.convertiraNumero(mensaje)
    cifrado = sustitucion.cifrar(cifrado, pos)
    mensajecifrado = sustitucion.convertiraLetra(cifrado)
    util.printResultado("cifrado",mensajecifrado)

def sustitucion_descifrar(mensaje_cifrado, pos): # Descifrar por Sustitución
    mensaje_cifrado = sustitucion.convertiraNumero(mensaje_cifrado)
    descifrado = sustitucion.descifrar(mensaje_cifrado, pos)
    mensajedescifrado = sustitucion.convertiraLetra(descifrado)
    util.printResultado("descifrado",mensajedescifrado)

def transposicion_cifrar(mensaje, clave):
    cifrado = transposicion.cifrar(mensaje, clave)
    util.printResultado("cifrado",cifrado)

def transposicion_descifrar(mensaje, clave):
    descifrado = transposicion.descifrar(mensaje, clave)
    util.printResultado("descifrado",descifrado)

if __name__ == '__main__':
    #main()
    test()