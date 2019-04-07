from django.db import models

class Usuario(models.Model):
    #Hacerle un FK a los tipos de usuario que ya esten definidos.
    tipo_usuario =  models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50)
    primer_nombre = models.CharField(max_length=)
