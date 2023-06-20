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
sum = p1+p2
mult = p1*p2
subs = p1-p2

polySuma=galois.Poly(sum)
polyMult = galois.Poly(mult)
print(polySuma)
print(sum)
print(polyMult)
print(mult)
