from django.urls import path
from .views import *

urlpatterns=[
    path('',vista_about, name='vista_about'),
    path('contacto/',vista_contacto, name='vista_contacto'),
    path('inicio/',vista_inicio, name='vista_inicio'),
    
    path('productos/',vista_productos, name='vista_productos'),
    path('agregar_productos/',vista_agregar_productos, name='vista_agregar_productos'),

]