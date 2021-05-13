from django.urls import path
from .views import *

urlpatterns=[
    path('',vista_about, name='vista_about'),
    path('contacto/',vista_contacto, name='vista_contacto'),
    path('inicio/',vista_inicio, name='vista_inicio'),
    
    path('productos/',vista_productos, name='vista_productos'),
    path('agregar_productos/',vista_agregar_productos, name='vista_agregar_productos'),

    path('ver_producto/<int:id_prod>', vista_ver_producto, name='vista_ver_producto'),
    path('eliminar_producto/<int:id_prod>', vista_eliminar_producto, name='vista_eliminar_producto'),
    path('editar_producto/<int:id_prod>', vista_editar_producto, name='vista_editar_producto'),

]