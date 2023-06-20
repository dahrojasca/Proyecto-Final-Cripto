import galois

#Se crea el campo finito. El del ejemplo de la expo era de 2^3
GF = galois.GF(2**3)

#Con esto accedemos a ls propiedades del campo finito. Lo que nos interesa es el polinomio irreducible
print("------Propiedades------"+"\n"+GF.properties)

#esto es cómo se representan todos los polinomios posibles con el campo finito que se definió
print("------Tabla representaciones------"+"\n"+GF.repr_table())

#Aquí se inicializan los polinomios con aquello de aritmética modular
p1 = galois.Poly([1, 1, 1], field= GF)  # Representa el polinomio x^2 + x + 1       → 1 1 1
p2 = galois.Poly([1, 0, 1], field= GF)  # Representa el polinomio x^2 + 1           → 1 0 1

#Operaciones que se pueden hacer con los polinomios sobre el campo finito
suma = p1+p2
#Con esto accedemos a los coeficientes del polinomio irreducible
irreducible_poly = GF.irreducible_poly
print("Coeficientes polinomio irreducible: ",GF.irreducible_poly.coefficients())

#Aquí tocó poner el polinomio irreducible como vector porque no supe extraerlo del irreducible_poly ↓
a = galois.Poly([1, 0, 1, 1], field=GF)

print("Polinomio 1: ",p1)
print("Polinomio 2: ",p2)

polySuma=p1+p2
polyMult = p1*p2%a
print("Suma: ",polySuma)
print("----")
print("Multiplicación pre-módulo",p1*p2)
print("Multiplicación post-módulo",polyMult)
