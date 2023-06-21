import galois

#Se crea el campo finito. El del ejemplo de la expo era de 2^3
GF = galois.GF(2**7)

#Con esto accedemos a ls propiedades del campo finito. Lo que nos interesa es el polinomio irreducible
print("------Propiedades------"+"\n"+GF.properties+"--------------------"+"\n")

#esto es cómo se representan todos los polinomios posibles con el campo finito que se definió
#print("------Tabla representaciones------"+"\n"+GF.repr_table())

palabra=input("Ingrese la palabra a cifrar: ");
palabraC = [ord(c) for c in palabra]
clave=input("Ingrese la clave: ")
claveC = [ord(c) for c in clave]

#Aquí se inicializan los polinomios con aquello de aritmética modular
p1 = galois.Poly(palabraC, field=GF)
print("Polinomio palabra: ",p1)
p2 = galois.Poly(claveC, field=GF)
print("Polinomio clave: ",p2)

#Operaciones que se pueden hacer con los polinomios sobre el campo finito
suma = p1+p2
#Con esto accedemos a los coeficientes del polinomio irreducible
irreducible_poly = GF.irreducible_poly
print("Coeficientes polinomio irreducible: ",GF.irreducible_poly.coefficients())

#Aquí tocó poner el polinomio irreducible como vector porque no supe extraerlo del irreducible_poly ↓
a = galois.Poly(GF.irreducible_poly.coefficients(), field=GF)

polySuma=p1+p2
polyMult = p1*p2%a
print("----Inicio-----")
print("Multiplicación pre-módulo",p1*p2)
print("Multiplicación post-módulo",polyMult)


numeros = polyMult.coefficients().tolist()
print(numeros)
for num in numeros:
    letra = chr((num%25)+65)
    print(letra, end="")

