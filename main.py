from desencriptado import desencriptar
from encriptado import encriptar

print("BIENVENIDO AL PROYECTO (con interfaz temporal)")
mode = int(input("Presiona 1 para encriptar, 0 para des"))

if mode == 1:    
    palabra=input("Ingrese la palabra a cifrar: ");
    clave=input("Ingrese la clave: ")
    print('El texto encriptado es:', encriptar(palabra, clave))

else:
    polinomio_encriptado = input("Ingrese los coeficientes del polinomio encriptado: ")
    clave = input("Ingrese la clave: ")

    print('El texto desencriptado es:', desencriptar(polinomio_encriptado, clave))