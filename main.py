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
        print("Polinomio palabra: ", p1)
        p2 = galois.Poly(claveC, field=GF)
        print("Polinomio clave: ", p2)

        a = galois.Poly(GF.irreducible_poly.coefficients(), field=GF)

        polySuma = p1 * p2
        polyMult = p1 * p2 % a

        numeros = polySuma.coefficients().tolist()
        numeros1 = polyMult.coefficients().tolist()

        print(numeros)
        for num in numeros1:
            letra = chr((num % 25) + 65)
            output = output + letra

        return output

class Decrypt:
    def __init__(self, polinomio_encriptado, clave):
        self.polinomio_encriptado = polinomio_encriptado[1:-1]
        self.clave = clave

    def decrypt(self):
        coeficientes = [int(x) for x in self.polinomio_encriptado.split(',')]
        polinomio_encriptado = galois.Poly(coeficientes, field=GF)
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
        word = request.form['word']
        key = request.form['key']
        encryptor = Encrypt(word, key)
        polynomial = encryptor.encrypt()
        return render_template('index.html', polynomial=polynomial)
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    polynomial = request.form['polynomial']
    key = request.form['key']
    decryptor = Decrypt(polynomial, key)
    decrypted_data = decryptor.decrypt()
    return render_template('decrypt.html', decrypted_data=decrypted_data)

if __name__ == '__main__':
    app.run()
