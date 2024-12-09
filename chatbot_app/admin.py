from django.contrib import admin
from .models import TipoLead, Programa, Momento, Submomento, Respuesta, Documento, Historial

@admin.register(Momento)
class MomentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'get_tipo_lead', 'programa')  # Mostrar 'tipo_lead' a través de programa
    list_filter = ('programa__tipo_lead', 'programa')  # Filtrar por tipo_lead y programa

    def get_tipo_lead(self, obj):
        return obj.programa.tipo_lead.nombre
    get_tipo_lead.short_description = "Tipo Lead"  # Etiqueta para la columna en el panel

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_lead')
    list_filter = ('tipo_lead',)

@admin.register(TipoLead)
class TipoLeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Submomento)
class SubmomentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'momento', 'programa', 'tipo_lead')
    list_filter = ('momento__programa__tipo_lead', 'programa', 'momento')

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido', 'prioridad', 'submomento')
    list_filter = ('submomento__tipo_lead', 'submomento__programa', 'submomento__momento')

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'archivo', 'fecha_carga')  # Asegúrate de que 'fecha_carga' exista
    list_filter = ('fecha_carga',)  # Asegúrate de que 'fecha_carga' exista
    search_fields = ('nombre', 'palabras_clave')

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'descripcion', 'fecha')  # Asegúrate de que 'descripcion' exista
    list_filter = ('usuario', 'fecha')
    search_fields = ('usuario', 'descripcion')
