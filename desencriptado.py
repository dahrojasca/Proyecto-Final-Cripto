import galois

GF = galois.GF(2**7)

# Ingresar el polinomio encriptado obtenido durante la encriptación
polinomio_encriptado = input("Ingrese el polinomio encriptado (coeficientes separados por espacios): ")
coeficientes = [int(x) for x in polinomio_encriptado.split()]
print(coeficientes)

#letras_encriptadas = input("Ingrese las letras encriptadas separadas por espacios: ").split()

#numeros = [ord(n) for n in letras_encriptadas]
#numeros_originales = []
# for i in numeros:
#     numeros_originales.append(pow(i,-1,25))



# for letra in letras_encriptadas:
#     numero = pow((ord(letra) - 65), -1, 25)
#     numeros.append(numero)

#print("AAAAAAAAAAAAAAAAAAA")
#print(numeros)
#print(numeros_originales)

# Crear un objeto Poly a partir de los coeficientes del polinomio encriptado
polinomio_encriptado = galois.Poly(coeficientes, field=GF)

clave=input("Ingrese la clave: ")
claveC = [ord(c) for c in clave]
polinomio_clave = galois.Poly(claveC, field=GF)
print("Polinomio clave: ",polinomio_clave)

# Obtener el polinomio irreducible del campo finito
polinomio_irreducible = galois.Poly(GF.irreducible_poly.coefficients(), field=GF)

print(polinomio_encriptado)
print(polinomio_irreducible)

polinomio_desencriptado = polinomio_encriptado//polinomio_clave

print(polinomio_desencriptado)

coeficientes_desencriptados = polinomio_desencriptado.coefficients()

# Convertir los coeficientes en números enteros
numeros_desencriptados = [int(x) for x in coeficientes_desencriptados]

# Convertir los números en caracteres ASCII
texto_desencriptado = ''.join(chr(x) for x in numeros_desencriptados)

print("Texto desencriptado:", texto_desencriptado)