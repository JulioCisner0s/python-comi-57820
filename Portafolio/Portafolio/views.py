from django.template import Template, Context

from django.http import HttpResponse
from datetime import datetime as dt
from django.template import loader


def saludo(request):
    return HttpResponse("Hello World!")

def julio(request):
    texto = "Soy Julio Cisneros Dev <br> pa"
    return HttpResponse(texto)

def dia_de_hoy (request, dia_personalizado):
    dia = dt.now()
    texto = f"Hoy es {dia.day} de {dia.month} de {dia.year}"
    dia = dia[:-2] + dia_personalizado
    return HttpResponse(texto)

def probando_template(request):
    
    nombre = "Julio"
    apellido = "Cisneros"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
        }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

