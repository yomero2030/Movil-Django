from rest_framework import routers, serializers, viewsets

#---------------- AGREGANDO MODELOS ---------------------
from Login.models import Login

class LoginSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Login
        fields = ('__all__')