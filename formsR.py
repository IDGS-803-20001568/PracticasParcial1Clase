from wtforms import Form, SelectField, RadioField

class ResistanceForm(Form):
    colores = [
        (0, 'Negro'),
        (1, 'Cafe'),
        (2, 'Rojo'),
        (3, 'Naranja'),
        (4, 'Amarillo'),
        (5, 'Verde'), 
        (6, 'Azul'),
        (7, 'Violeta'),
        (8, 'Gris'),
        (9, 'Blanco'),
    ]
    tolerancias = [
        (5, 'Dorado'), 
        (10, 'Plata')
    ]

    color1 = SelectField('Color 1', choices=colores)
    color2 = SelectField('Color 2', choices=colores)
    color3 = SelectField('Color 3', choices=colores)
    tolerancia = RadioField('Tolerancia', choices=tolerancias)
