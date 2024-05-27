def cifrar(mensaje, clave):
    mensaje = mensaje.replace(" ", "")
    filas = len(mensaje) // clave
    if len(mensaje) % clave != 0:
        filas += 1
        mensaje += "*" * (clave - (len(mensaje) % clave))  # Añadir caracteres extras al mensaje
    cifrado = ""
    for j in range(clave):
        for i in range(filas):
            cifrado += mensaje[i * clave + j]
    return cifrado

def descifrar(mensaje_cifrado, clave):
    mensaje_cifrado = mensaje_cifrado.replace(" ", "")
    filas = len(mensaje_cifrado) // clave
    descifrado = ""
    for i in range(filas):
        for j in range(clave):
            descifrado += mensaje_cifrado[i + j * filas]
    # Eliminar caracteres extras agregados
    descifrado = descifrado.rstrip("*")
    return descifrado
