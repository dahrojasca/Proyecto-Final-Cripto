import galois

GF = galois.GF(2**7)

def desencriptar(polinomio_encriptado, clave):
    # Ingresar el polinomio encriptado obtenido durante la encriptación
    polinomio_encriptado = polinomio_encriptado[1:-1]
    coeficientes = [int(x) for x in polinomio_encriptado.split(',')]

    # Crear un objeto Poly a partir de los coeficientes del polinomio encriptado
    polinomio_encriptado = galois.Poly(coeficientes, field=GF)

    claveC = [ord(c) for c in clave]
    polinomio_clave = galois.Poly(claveC, field=GF)
    # print("Polinomio clave: ",polinomio_clave)

    # Obtener el polinomio irreducible del campo finito
    # polinomio_irreducible = galois.Poly(GF.irreducible_poly.coefficients(), field=GF)

    # print(polinomio_encriptado)
    # print(polinomio_irreducible)

    polinomio_desencriptado = polinomio_encriptado//polinomio_clave

    # print(polinomio_desencriptado)

    coeficientes_desencriptados = polinomio_desencriptado.coefficients()

    # Convertir los coeficientes en números enteros
    numeros_desencriptados = [int(x) for x in coeficientes_desencriptados]

    # Convertir los números en caracteres ASCII
    texto_desencriptado = ''.join(chr(x) for x in numeros_desencriptados)

    return texto_desencriptado
