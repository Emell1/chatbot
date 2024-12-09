from django.http import JsonResponse
from .models import TipoLead, Programa, Momento, Submomento, Historial

def get_tipo_lead(request):
    print("Solicitud recibida en obtener_tipo_leads")
    tipos = list(TipoLead.objects.values('id', 'nombre'))
    return JsonResponse({'tipos': tipos})

def get_programa(request):
    tipo_lead_id = request.GET.get('tipo_lead_id')
    print (tipo_lead_id)
    programas = list(Programa.objects.filter(tipo_lead_id=tipo_lead_id).values('id', 'nombre'))
    return JsonResponse({'programas': programas})

def get_momento(request):
    programa_id = request.GET.get('programa_id')
    momentos = list(Momento.objects.filter(programa_id=programa_id).values('id', 'nombre'))
    return JsonResponse({'momentos': momentos})

def get_submomento(request):
    momento_id = request.GET.get('momento_id')
    submomentos = list(Submomento.objects.filter(momento_id=momento_id).values('id', 'nombre'))
    return JsonResponse({'submomentos': submomentos})

def get_historial(request):
    historial = list(Historial.objects.values('id', 'descripcion', 'fecha'))
    return JsonResponse({'historial': historial})

def nueva_conversacion(request):
    # Lógica para reiniciar la conversación
    return JsonResponse({'status': 'Nueva conversación iniciada'})
