from django.urls import path
from .views import *

urlpatterns=[
    path('',vista_about, name='vista_about'),
    path('contacto/',vista_contacto, name='vista_contacto'),
    path('inicio/',vista_inicio, name='vista_inicio'),
]