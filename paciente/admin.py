from django.contrib import admin

from .models import Paciente
from .models import Usuario

#Esta clase me muestra los parámetros que le indique.
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','numero_emergencia', 'primer_nombre', 'primer_apellido', 'fecha_de_nacimiento', 'telefono',
                    'tipo_de_sangre', 'sexo', 'estado_tratamiento', 'usuario')
    list_display_links = ('id', 'usuario')
    list_filter = ('estado_tratamiento',)
    list_editable = ('estado_tratamiento',)
    list_per_page = 25
    def primer_nombre(self, obj):
        return obj.usuario.primer_nombre
    def primer_apellido(self, obj):
        return obj.usuario.primer_apellido
    def fecha_de_nacimiento(self, obj):
        return obj.usuario.fecha_nacimiento
    def telefono(self, obj):
        return obj.usuario.telefono
    def tipo_de_sangre(self, obj):
        return obj.usuario.grupo_sanguineo
    def sexo(self, obj):
        return obj.usuario.sexo
admin.site.register(Paciente, PacienteAdmin)





