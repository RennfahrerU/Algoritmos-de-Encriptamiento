import time
def pedirmsj(entrada:str):
    mensaje = input(f'{entrada}')
    # Convierte el String a mayúsculas para coincidir con los diccionarios
    mensaje = mensaje.upper()
    print("El mensaje es: " + mensaje)
    return mensaje

def printResultado(operacion,mensaje):
        print(f"El mensaje {operacion} es: " + mensaje)
        time.sleep(1)
