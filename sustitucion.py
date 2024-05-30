abecedario = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
              'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

abecedario_inverso = {valor: clave for clave, valor in abecedario.items()}

def convertiraNumero(mensaje):
    cifrado = []
    for letra in mensaje.upper():
        if letra in abecedario:
            cifrado.append(abecedario[letra])
    return cifrado

def cifrar(cifrado, pos):
    for i in range(len(cifrado)):
        cifrado[i] = (cifrado[i] + pos) % 27
    return cifrado

def descifrar(cifrado, pos):
    for i in range(len(cifrado)):
        cifrado[i] = (cifrado[i] - pos) % 27
    return cifrado

def convertiraLetra(cifrado):
    mensajecifrado = ''
    for numero in cifrado:
        mensajecifrado += abecedario_inverso[numero]
    return mensajecifrado
