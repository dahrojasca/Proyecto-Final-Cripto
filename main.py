from flask import Flask, render_template, request
import galois

app = Flask(__name__)

GF = galois.GF(2**7)

class Encrypt:
    def __init__(self, palabra, clave):
        self.palabra = palabra
        self.clave = clave

    def encrypt(self):
        palabraC = [ord(c) for c in self.palabra]
        claveC = [ord(c) for c in self.clave]
        output = ""

        p1 = galois.Poly(palabraC, field=GF)
        print("Polinomio palabra:", p1)  # Print the polynomial object

        p2 = galois.Poly(claveC, field=GF)
        print("Polinomio clave:", p2)

        a = galois.Poly(GF.irreducible_poly.coefficients(), field=GF)

        polySuma = p1 * p2
        polyMult = p1 * p2 % a

        numeros = polySuma.coefficients().tolist()
        numeros1 = polyMult.coefficients().tolist()

        print(numeros)
        for num in numeros1:
            letra = chr((num % 25) + 65)
            output = output + letra

        # print("estossonlosnumeros",numeros)

        return output, numeros, polySuma  # Return the output string and the polynomial object


class Decrypt:
    def __init__(self, polinomio_encriptado, clave):
        self.polinomio_encriptado = polinomio_encriptado
        self.clave = clave

    def decrypt(self):
        polinomio_encriptado = galois.Poly(self.polinomio_encriptado, field=GF)
        claveC = [ord(c) for c in self.clave]
        polinomio_clave = galois.Poly(claveC, field=GF)
        polinomio_desencriptado = polinomio_encriptado // polinomio_clave
        coeficientes_desencriptados = polinomio_desencriptado.coefficients()
        numeros_desencriptados = [int(x) for x in coeficientes_desencriptados]
        texto_desencriptado = ''.join(chr(x) for x in numeros_desencriptados)
        return texto_desencriptado


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'word' in request.form and 'key' in request.form:
            word = request.form['word']
            key = request.form['key']
            encryptor = Encrypt(word, key)
            output, polynomial, polysuma = encryptor.encrypt()
            return render_template('index.html', polynomial=polynomial, output=output, polysuma=polysuma)
        elif 'polynomial' in request.form and 'decrypt_key' in request.form:
            polynomial = request.form['polynomial']
            polynomial = polynomial[1:-1]
            polynomial = ([int(x) for x in polynomial.split(',')])
            # print(polynomial)
            # print(type(polynomial))
            key = request.form['decrypt_key']
            decryptor = Decrypt(polynomial, key)
            decrypted_data = decryptor.decrypt()
            # print(decrypted_data)
            # print(type(decrypted_data))
            return render_template('index.html', polynomial=polynomial, decrypted_data=decrypted_data, polysuma=polysuma)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
