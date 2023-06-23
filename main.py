from flask import Flask, render_template, request
import galois

app = Flask(__name__)

GF = galois.GF(2**7)

# Clase para encriptar
class Encrypt:
    # Constructor de la clase con los parametros palabra y clave
    def __init__(self, palabra, clave): 
        self.palabra = palabra # Se asigna el parametro palabra a la variable palabra de la clase
        self.clave = clave # Se asigna el parametro clave a la variable clave de la clase

    def encrypt(self):
        palabraC = [ord(c) for c in self.palabra] # Se convierte la palabra a una lista de numeros
        claveC = [ord(c) for c in self.clave] # Se convierte la clave a una lista de numeros
        output = ""

        p1 = galois.Poly(palabraC, field=GF) # Se crea el polinomio de la palabra
        print("Polinomio palabra:", p1)

        p2 = galois.Poly(claveC, field=GF) # Se crea el polinomio de la clave
        print("Polinomio clave:", p2)

        a = galois.Poly(GF.irreducible_poly.coefficients(), field=GF) # Se crea el polinomio irreducible

        polySuma = p1 * p2 # Se multiplican los polinomios
        polyMult = p1 * p2 % a # Se aplica el modulo al resultado de la multiplicacion

        numeros = polySuma.coefficients().tolist() # Se convierte el polinomio de la suma a una lista de numeros
        numeros1 = polyMult.coefficients().tolist() # Se convierte el polinomio de la multiplicacion a una lista de numeros

        print(numeros)
        # Se convierten los numeros a letras
        for num in numeros1:
            letra = chr((num % 25) + 65)
            output = output + letra

        # print("estossonlosnumeros",numeros)

        return output, numeros, polySuma  # Return the output string and the polynomial object


class Decrypt:
    # Constructor de la clase con los parametros polinomio_encriptado y clave
    def __init__(self, polinomio_encriptado, clave): 
        self.polinomio_encriptado = polinomio_encriptado
        self.clave = clave

    # Metodo para desencriptar
    def decrypt(self): 
        polinomio_encriptado = galois.Poly(self.polinomio_encriptado, field=GF) # Se crea el polinomio encriptado
        claveC = [ord(c) for c in self.clave] # Se convierte la clave a una lista de numeros
        polinomio_clave = galois.Poly(claveC, field=GF) # Se crea el polinomio de la clave
        
        # Se divide el polinomio encriptado entre el polinomio de la clave
        polinomio_desencriptado = polinomio_encriptado // polinomio_clave 
        
        # Se obtienen los coeficientes del polinomio desencriptado
        coeficientes_desencriptados = polinomio_desencriptado.coefficients()
        
        # Se convierten los coeficientes a numeros
        numeros_desencriptados = [int(x) for x in coeficientes_desencriptados]
        texto_desencriptado = ''.join(chr(x) for x in numeros_desencriptados)
        return texto_desencriptado


@app.route('/', methods=['GET', 'POST'])
# Metodo para renderizar el template index.html
def index():
    if request.method == 'POST':
        if 'word' in request.form and 'key' in request.form:
            word = request.form['word'] # Se obtiene la palabra del formulario
            key = request.form['key'] # Se obtiene la clave del formulario
            encryptor = Encrypt(word, key) # Se crea el objeto encryptor de la clase Encrypt
            output, polynomial, polysuma = encryptor.encrypt() # Se encripta la palabra
            
            # Se renderiza el template index.html con los parametros polynomial, output y polysuma
            return render_template('index.html', polynomial=polynomial, output=output, polysuma=polysuma)
        
        # Si se quiere desencriptar
        elif 'polynomial' in request.form and 'decrypt_key' in request.form:
            polynomial = request.form['polynomial'] # Se obtiene el polinomio encriptado del formulario
            polynomial = polynomial[1:-1] # Se quitan los corchetes del polinomio
            polynomial = ([int(x) for x in polynomial.split(',')]) # Se convierte el polinomio a una lista de numeros
            # print(polynomial)
            # print(type(polynomial))
            key = request.form['decrypt_key'] # Se obtiene la clave del formulario
            decryptor = Decrypt(polynomial, key) # Se crea el objeto decryptor de la clase Decrypt
            decrypted_data = decryptor.decrypt() # Se desencripta el polinomio
            # print(decrypted_data)
            # print(type(decrypted_data))
            
            # Se renderiza el template index.html con los parametros polynomial y decrypted_data
            return render_template('index.html', polynomial=polynomial, decrypted_data=decrypted_data) 
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
