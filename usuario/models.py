import os

from django.db import models
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

from btre_project import settings


class Usuario(SafeDeleteModel):
    SEX_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    GENTILICIOS = (
        ('RD', 'Dominicano'),
        ('HT', 'Haitiano'),
        ('USA', 'Estadounidense'),
        ('CU', 'Cubano'),
    )
    SANGRE = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    TIPO_CHOICE = (
        ('PA', 'Paciente'),
        ('EM', 'Empleado')
    )
    #Hacerle un FK a los tipos de usuario que ya esten definidos.
    tipo_usuario = models.CharField(max_length=3, choices=TIPO_CHOICE)
    nombre_usuario = models.CharField(max_length=50)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    cedula = models.CharField(max_length=13, default='000-0000000-0', unique=True)
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    grupo_sanguineo = models.CharField(max_length=4, choices=SANGRE)
    linea_direccion_1 = models.CharField(max_length=120)
    linea_direccion_2 = models.CharField(max_length=120, blank=True)
    sector = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=120)
    pais = CountryField()
    nacionalidad = models.CharField(max_length=75, choices=GENTILICIOS)
    nss = models.CharField(max_length=13)
    foto_perfil = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    _safedelete_policy = SOFT_DELETE_CASCADE
    deleted = models.DateTimeField(null=True, blank=True, editable=False)
    def __str__(self):
        return self.cedula

