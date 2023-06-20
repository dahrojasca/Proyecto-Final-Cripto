import galois

#Se crea el campo finito. El del ejemplo de la expo era de 2^3
GF = galois.GF(2**3)

#Con esto accedemos a ls propiedades del campo finito. Lo que nos interesa es el polinomio irreducible

print("------Propiedades------"+"\n"+GF.properties)

#esto es cómo se representan todos los polinomios posibles con el campo finito que se definió
print("------Tabla representaciones------"+"\n"+GF.repr_table())

#Aquí se inicializan los polinomios con aquello de aritmética modular
p1 = GF([1, 1, 1])  # Representa el polinomio x^2 + x + 1       → 1 1 1
p2 = GF([1, 0, 1])  # Representa el polinomio x^2 + 1           → 1 0 1

#Operaciones que se pueden hacer con los polinomios sobre el campo finito
suma = p1+p2
irreducible_poly = GF.irreducible_poly
print("Coeficientes polinomio irreducible: ",GF.irreducible_poly.coefficients())
multiplication = (p1*p2)#%GF.irreducible_poly.coefficients()
subs = p1-p2

print("Polinomio 1: ",galois.Poly(p1))
print("Polinomio 2: ",(galois.Poly(p2)))

polySuma=galois.Poly(suma)
polyMult = galois.Poly(multiplication)
print("Suma: ",polySuma)
print("----")
print("Multiplicación",polyMult)
