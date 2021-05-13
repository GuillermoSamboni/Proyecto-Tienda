from rest_framework import serializers
from home.models import *
#from .serializer import *

# Create your views here.

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Producto
        fields=('url','nombre','descripcion','status','precio','stok','marca','Categorias',)

class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Marca
        fields=('url','nombre')

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Categoria
        fields=('url','nombre')
