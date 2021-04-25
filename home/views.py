from django.shortcuts import render
from .forms import *


# Create your views here.
def vista_about(request):
    return render(request, 'about.html', locals())


def vista_inicio(request):
    return render(request, 'inicio.html', locals())



def vista_contacto(request):
    info_enviado= False
    email = ""
    title = ""
    text = ""
    if request.method == "POST":
        formulario= contacto_form(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email= formulario.cleaned_data["correo"]
            title= formulario.cleaned_data["titulo"]
            text= formulario.cleaned_data["texto"]
    else:
        formulario = contacto_form()
    return render(request, 'contacto.html', locals())

