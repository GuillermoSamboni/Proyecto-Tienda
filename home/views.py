from django.shortcuts import render, redirect
from .forms import *
from .models import *


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

def vista_productos(request):
    productos = Producto.objects.filter() #SELECT FROM *

    return render(request, 'productos.html', locals())


def vista_agregar_productos(request):
    if request.method =='POST':
        formulario=agregar_producto_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/')
    else:    
        formulario = agregar_producto_form()


    return render(request,'agregarProducto.html', locals())
