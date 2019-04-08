from django.contrib import admin

from .models import Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'primer_nombre', 'primer_apellido')
    list_per_page = 25

admin.site.register(Usuario, UsuarioAdmin)
