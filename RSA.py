import random

# Función para calcular el máximo común divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para calcular la inversa modular
def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    
    if m == 1:
        return 0
    
    while a > 1:
        q = a // m
        t = m
        
        m = a % m
        a = t
        t = y
        
        y = x - q * y
        x = t
        
    if x < 0:
        x += m0
        
    return x

# Generar claves RSA
def gen_keys(bits):
    while True:
        # Generar primos p y q
        p = gen_prime(bits // 2)
        q = gen_prime(bits // 2)
        
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # Elegir e coprimo con phi
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
            
        # Calcular d
        d = mod_inverse(e, phi)
        
        # Verificar si las claves funcionan
        test_msg = 12345
        cipher = encrypt_number(test_msg, e, n)
        decrypted = decrypt_number(cipher, d, n)
        if decrypted == test_msg:
            return (e, d, n)

# Cifrar un mensaje
def encrypt(msg, e, n):
    cipher = []
    for char in msg:
        cipher.append(pow(ord(char), e, n))
    return cipher

# Descifrar un mensaje
def decrypt(cipher, d, n):
    msg = ''
    for c in cipher:
        char = pow(c, d, n)
        if char in range(32, 127):  # Rango de caracteres ASCII válidos
            msg += chr(char)
    return msg

# Cifrar un número
def encrypt_number(num, e, n):
    return pow(num, e, n)

# Descifrar un número
def decrypt_number(cipher, d, n):
    return pow(cipher, d, n)

# Generar un número primo
def gen_prime(bits):
    while True:
        p = random.randrange(2 ** (bits - 1), 2 ** bits)
        if is_prime(p):
            return p

# Verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
