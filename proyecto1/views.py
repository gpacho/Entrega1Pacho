
from django.http import HttpResponse


def hola(request):
    return HttpResponse("<h1>Nashenashe</h1>")
    