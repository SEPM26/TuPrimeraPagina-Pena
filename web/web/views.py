from django.template import Template, Context
from django.http import HttpResponse

def Template (self):

    miHtml = open("C:\Users\Sebastián\Desktop\Web1\web\app\templates\index.html")

    plantilla = Template(miHtml.red())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse (documento)