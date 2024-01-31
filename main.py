from flask import Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route("/")
def index():
    escuela="UTL!!!"
    alumnos=["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/maestros")
def maes():
    return render_template("maestros.html")


@app.route("/hola")
def hola():
    return "<p> <h1> Hola desde  HOLA!!! <br> Mundo</h1> </p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola"+name

@app.route("/numero/<int:n>")
def numero(n):
    return "En numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID: {} Nombre: {}".format(id,name)

@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1,n2):
    return "el valor de {} + {} = {}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def func2(ab="UTL"):
    return "El valor es: "+ab

@app.route("/multiplicar",methods=["GET","POST"])
def mult():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return"<h1>La Multiplicacion es: {}</h1>".format(str(int(num1)*int(num2)))
    else:
     return '''
    <form action="/multiplicar" method="POST">
    <label>N1:</label>
    <input type="text" name="n1"/><br>
     <label>N2:</label>
    <input type="text" name="n2"/><br>
    <input type="submit"/>    
    </form>

    '''

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    if request.method == "POST":
        num1 = float(request.form.get("n1"))
        num2 = float(request.form.get("n2"))
        suma = "sum" in request.form
        resta = "res" in request.form
        multiplicacion = "mult" in request.form
        division = "div" in request.form
        result = ""
        if suma:
            result += f"Suma: {num1 + num2} "
        if resta:
            result += f"Resta: {num1 - num2} "
        if multiplicacion:
            result += f"Multiplicación: {num1 * num2} "
        if division and num2 != 0:
            result += f"División: {num1 / num2} "

        return f"<h1>{result}</h1>"


@app.route("/cinepolis", methods=["POST"])
def cinepolis():
    if request.method == "POST":
        cte = request.form.get("cte")
        compradores = int(request.form.get("compradores"))
        tiene_tarjeta = request.form.get("tarjeta") == "si"
        boletos = int(request.form.get("boletos"))
        
        if boletos > 7:
            return jsonify({'error': 'No puedes comprar más de 7 boletos'})

        precio_base = 12
        descuento = 0

        if boletos > 5:
            descuento += 0.15
        elif 3 <= boletos <= 5:
            descuento += 0.1

        if tiene_tarjeta:
            descuento += 0.1

        valor_pagar = precio_base * boletos * (1 - descuento)

        return jsonify({'valor_pagar': valor_pagar})

    return render_template("cinepolis.html")

if __name__=="__main__":
    app.run(debug=True)