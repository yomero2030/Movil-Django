from rest_framework import routers, serializers, viewsets

from producto.models import Producto



class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = ('__all__')