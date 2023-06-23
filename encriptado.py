import galois

#Se crea el campo finito. El del ejemplo de la expo era de 2^3
GF = galois.GF(2**7)

def encriptar(palabra, clave):
    palabraC = [ord(c) for c in palabra]
    claveC = [ord(c) for c in clave]
    output=""

    #Aquí se inicializan los polinomios con aquello de aritmética modular
    p1 = galois.Poly(palabraC, field=GF)
    p2 = galois.Poly(claveC, field=GF)

    #Aquí tocó poner el polinomio irreducible como vector porque no supe extraerlo del irreducible_poly ↓
    a = galois.Poly(GF.irreducible_poly.coefficients(), field=GF)

    polySuma=p1*p2
    polyMult = p1*p2%a
    # print("Multiplicación pre-módulo",p1*p2)
    # print("Multiplicación post-módulo",polyMult)
    numeros = polySuma.coefficients().tolist()
    numeros1 = polyMult.coefficients().tolist()
    print(numeros)
    for num in numeros1:
        letra = chr((num%25)+65)
        output = output+letra
    
    return output