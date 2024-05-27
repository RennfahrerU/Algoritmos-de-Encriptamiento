abecedario = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
              'N': 14, 'Ñ': 15, 'O': 16, 'P': 17, 'Q': 18, 'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25, 'Y': 26, 'Z': 27}

abecedario_inverso = {valor: clave for clave, valor in abecedario.items()}

def convertiraNumero(mensaje):
    cifrado = []
    for letra in mensaje:  # Por cada letra que haya en mensaje
        if letra in abecedario:  # Por cada letra del mensaje que coincida con una letra del diccionario
            # Añade la equivalente numérica de la letra mencionada a la lista de valores cifrada
            cifrado.append(abecedario[letra])
    return cifrado


def cifrar(cifrado, pos):
    # Para i en el rango de la lista cifrada, se utiliza range porque la variable i toma los índices de los elementos de la lista en lugar de los valores.
    for i in range(len(cifrado)):
        # Se toma el valor de cifrado y se le suma pos, se resta 1 porque el abecedario comienza en 1. Se saca módulo 27 para ver si sobrepasa de este para reiniciar la cuenta. Se agrega 1 nuevamente para no quedar en posición 0.
        cifrado[i] = (cifrado[i] + pos - 1) % 27 + 1
    return cifrado

def descifrar(cifrado, pos):
    # Para i en el rango de la lista cifrada, se utiliza range porque la variable i toma los índices de los elementos de la lista en lugar de los valores.
    for i in range(len(cifrado)):
        # Se toma el valor de cifrado y se le suma pos, se resta 1 porque el abecedario comienza en 1. Se saca módulo 27 para ver si sobrepasa de este para reiniciar la cuenta. Se agrega 1 nuevamente para no quedar en posición 0.
        cifrado[i] = (int(cifrado[i]) - pos - 1) % 27 + 1
    return cifrado

def convertiraLetra(cifrado):
    mensajecifrado = ''  # Se define como un string vacío de momento
    for numero in cifrado:  # Por cada número que haya en cifrado
        # La letra es igual al abecedario inverso de acuerdo al número
        letra = abecedario_inverso[numero]
        mensajecifrado += letra  # Agrega la letra obtenida de el diccionario al String
    return mensajecifrado