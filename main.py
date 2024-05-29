import sustitucion
import transposicion
import util
import RSA

def main():
    mensaje = util.pedirmsj("Ingrese el mensaje a operar: ")
    mensaje_cifrado = RSA_cifrar(mensaje)
    RSA_descifrar(mensaje_cifrado)

    #RSA_cifrar(mensaje)
    #RSA_descifrar(b"\x82\xaf^\xe0\r{\xff\xb1\xeb\x85\x03u\x16\xe2\x07!\x1ap*\xb6\xbd\x92\xfd\x8d?\xf1\xc9\xe9!\x87\x16]\\kIF<(\xedp\xac;\x837\xc7\x1e\x92\x8d\xe1:\xa7D\xdeVq\xa5\xef\xe2\x86\xc2p\xa67\x00!G\x94(\xc7\xde\x11\xd8K{F\xd2\xfaP\xaf\x0ey2K\xd8\xad.H\x91Mc\xbfG\xe1\x93\x9dQ\xf3\xa0\x0f[1K\xd4\xcb\xfe\xeb\x9f\xee\x1b4\xc3\xdb(a\xd1\xa9xp\xdaj\xb8\x0b\x98\n\xabt\x1d,.\xc1s\xd7\x9dm\x13\xa9\x95h7cp\xfb\x08;M\x9d\xc31w\xb6\xcd\x9b\xa0\x8f]\x1f4\x1b\xd5L\x14\x0b-\x7f\xda\x87\xdb\x06\xe3\xc5\x027\xab\xfd\xc6\xd8\\=\xb6\x0f;5n'I7\xaed\x02\xd9\x98m\xa3\xdfR\xcc\x87\x8bJ\xb0\x8c\x82\xe5\xa35\x14C\xb9D:{\xf5xE\x07Y\x84A\xf5\xde\x19\xd9D\x88\xcfpS\xe8v\xcf\x17\x1f_\xfd\xb1\xcb\xa2\r\xd8\xa6\xc1\xcdO}\x1f\x98\x15>\x9e\xebU\xabD\xad \t")
    #RSA_descifrar(b'\x81\xc7;\x91\xb0\xa3w\xfd\xa8o\xb6\xb5L\xd8\n\xc6\xed\xf6\xef\xbc \xa9\xf3`\xa7\xa2\xf2\xc8\x9d\x17b\x025\x9c\xa9\xd2\x03\xe5\xf2\xf5\xe0M\xaf\xd1\x83\x0f\x8eO\x85\xc8\xac\xa77\xd5\x12\x14\xbe\xc64+\x17\x01\x8a\xadBO\xee+\xe0eeITd\x14d\x8e\xca\x95\x90v\x80Qk\x1cL\x98\x01un\xb2\xdc\n\xcc\xb50hX\xc4\xf3\xd4G\x1eM\x1d\x1c\xd9\x84\x18\xda\xb3\xc8\xd2<;\x82\xd4\x04J\xad2\xe7\xceLD0\xf73`\xac\xb7\x15\x147.\x16X\x8c\x86\xf1\xcfM\x0e\xb1\xce\xec\x82Uu\x95\x9b\x9a\xc9\t`s\xb3a\x91v\xcb\xfe\xfd_\x89\xe5\x9f\xf4\xdb/{\xfe\xce\xd6qgf"CP\xb2.\xc6\xc3v\x7fs\xda\xd0\x7f\xc0\x94Z\xcfJ\xfb\xd4\x04\xeb\x9f\x9d\xfc"\'\xfe\xde\xef\xa0l\x87\xb9]\x99\xec!\xbf\xf4\xbb\xa9\xab@\xc6\xc1f\rvV:\x95\x02\xd4\xed\x0e\xa6\xf9\xa6+\xd7\xf0\xb1,9\x93\x9f\xa8?\xac\x8ax\x17X\xbd\n\xeax\xdb')
    
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

def RSA_cifrar(mensaje):
    mensaje_bytes = mensaje.encode(encoding='UTF-8',errors='strict')
    mensaje_cifrado = RSA.cifrar(mensaje_bytes)
    print(f'Mensaje cifrado: \n {mensaje_cifrado}')
    return mensaje_cifrado

def RSA_descifrar(mensaje_cifrado):
    # mensaje_bytes = mensaje.encode(encoding='UTF-8',errors='strict')
    mensaje_descifrado = RSA.descifrar(mensaje_cifrado)
    mensaje_descifrado = mensaje_descifrado.decode()
    print(mensaje_descifrado)

if __name__ == '__main__':
    #main()
    test()