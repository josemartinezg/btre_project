from datetime import datetime
from usuario.models import Usuario
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

#Creando modelos:Listings > models.py

class Paciente(SafeDeleteModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, unique=True)
    numero_emergencia = models.CharField(max_length=200)
    antecedentes_patologicos = models.TextField(blank=True)
    antecedentes_hereditarios = models.TextField(blank=True)
    antecedentes_alergicos = models.TextField(blank=True)
    estado_tratamiento = models.BooleanField(default=True)
    _safedelete_policy = SOFT_DELETE_CASCADE
    deleted = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.usuario.nombre_usuario

