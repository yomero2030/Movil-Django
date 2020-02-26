from django.db import models
from django.utils import timezone
# Create your models here.


class Producto(models.Model):
    name = models.CharField(max_length=254, null = False)
    precio = models.IntegerField(null = False)
    descripcion = models.CharField(max_length=254, null=False )
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)


    def _str_(self):
        return self.name

    class Meta: 
        db_table = 'producto'