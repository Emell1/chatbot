from django.db import models

class TipoLead(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_lead = models.ForeignKey(TipoLead, on_delete=models.CASCADE, related_name="programas")

    def __str__(self):
        return f"{self.nombre} ({self.tipo_lead.nombre})"


class Momento(models.Model):
    nombre = models.CharField(max_length=100)
    respuesta_momento = models.TextField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="momentos")

    def __str__(self):
        return f"{self.nombre} ({self.programa.nombre})"


class Submomento(models.Model):
    nombre = models.CharField(max_length=100)
    momento = models.ForeignKey(Momento, on_delete=models.CASCADE, related_name="submomentos")
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    tipo_lead = models.ForeignKey(TipoLead, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.momento.nombre} - {self.programa.nombre})"


class Respuesta(models.Model):
    contenido = models.TextField()
    prioridad = models.IntegerField()
    submomento = models.ForeignKey(Submomento, on_delete=models.CASCADE, related_name="respuestas")

    def __str__(self):
        return f"Respuesta para {self.submomento.nombre} - Prioridad: {self.prioridad}"


class Documento(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='documentos/')
    palabras_clave = models.TextField()
    fecha_carga = models.DateTimeField(auto_now_add=True)  # Agregando el campo faltante

    def __str__(self):
        return self.nombre




# models.py
from django.db import models

class Historial(models.Model):
    momento = models.CharField(max_length=100)
    submomento = models.CharField(max_length=100, blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    session_id = models.CharField(max_length=255)  # Identificador único de la sesión
    timestamp = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)  # O ForeignKey si está relacionado a un modelo de usuario
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.momento} - {self.submomento} ({self.session_id})"
