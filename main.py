from flask import Flask,render_template,request,jsonify
import forms
import math
from formsR import ResistanceForm

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


@app.route("/cinepolis", methods=["GET", "POST"])
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



@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    alum_form = forms.UserForm(request.form)

    if request.method == 'POST' and alum_form.validate():
        x1 = float(alum_form.x1.data)
        x2 = float(alum_form.x2.data)
        y1 = float(alum_form.y1.data)
        y2 = float(alum_form.y2.data)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        alum_form.resultado.data = distance

        print("Resultado:", alum_form.resultado.data)

        return render_template("distancia.html", form=alum_form)

    return render_template("distancia.html", form=alum_form)



color_css_mapping = {
    'Cafe': 'cafe',
    'Rojo': 'rojo',
    'Naranja': 'naranja',
    'Negro': 'negro',
    'Amarillo': 'amarillo',
    'Azul': 'azul',
    'Violeta': 'violeta',
    'Gris': 'gris',
    'Verde': 'verde',
    'Blanco': 'blanco'
}


@app.route("/resistencia",methods=["GET","POST"])
def res():
    operadores = {
        0: 1,
        1: 10,
        2: 100,
        3: 1000,
        4: 10000,
        5: 100000,
        6: 1000000,
        7: 10000000,
        8: 100000000,
        9: 1000000000
    }
    colores = {
        0: 'Negro',
        1: 'Cafe',
        2: 'Rojo',
        4: 'Amarillo',
        3: 'Naranja',
        5: 'Verde', 
        6: 'Azul',
        7: 'Violeta',
        8: 'Gris',
        9: 'Blanco',
    }
    registro = []
    color1_nombre = ""
    color2_nombre = ""
    color3_nombre = ""
    tolerancia = 0
    resistenciaT = 0
    resistenciaMin = 0
    resistenciaMax = 0
    porcentaje_tolerancia = 0.0
    resistencia_form = ResistanceForm(request.form) 
    
    if request.method == 'POST':
        color1 = int(resistencia_form.color1.data)
        color2 = int(resistencia_form.color2.data)
        color3 = int(resistencia_form.color3.data)
        tolerancia = int(resistencia_form.tolerancia.data)
        
        color1_nombre = colores[color1]
        color2_nombre = colores[color2]
        color3_nombre = colores[color3]
        
        concat = str(color1) + str(color2)
        resistenciaT = int(concat) * operadores.get(color3, 1)
        porcentaje_tolerancia = resistenciaT * (tolerancia / 100)
        resistenciaMin = resistenciaT - porcentaje_tolerancia
        resistenciaMax = resistenciaT + porcentaje_tolerancia

    return render_template("resistencia.html", form=resistencia_form, color1=color1_nombre, color2=color2_nombre, color3=color3_nombre, tolerancia=tolerancia, resistenciaT=resistenciaT ,resistenciaMin=resistenciaMin, resistenciaMax=resistenciaMax, color_css_mapping=color_css_mapping)

 
if __name__=="__main__":
    app.run(debug=True)