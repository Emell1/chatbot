from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TipoLead, Programa, Momento, Submomento, Respuesta, Historial

def get_tipo_lead(request):
    tipos = list(TipoLead.objects.values('id', 'nombre'))
    return JsonResponse({'tipos': tipos})

@csrf_exempt
def get_programa(request):
    print("-----> programa")
    if request.method == 'GET':
        tipo_lead_id = request.GET.get('tipo_lead_id')
        programas = Programa.objects.filter(tipo_lead_id=tipo_lead_id)
        print("----->", programas)
        data = [{"id": p.id, "nombre": p.nombre} for p in programas]
        return JsonResponse({"programas": data})

@csrf_exempt
def get_momento(request):
    print("-----> momento")
    if request.method == 'GET':
        programa_id = request.GET.get('programa_id')
        print("----->", programa_id)
        momentos = Momento.objects.filter(programa_id=programa_id)
        print("----->", momentos)
        data = [{"id": m.id, "nombre": m.nombre} for m in momentos]
        return JsonResponse({"momentos": data})

def get_submomento(request):
    momento_id = request.GET.get('momento_id')
    submomentos = Submomento.objects.filter(momento_id=momento_id).values('id', 'nombre')
    return JsonResponse({'submomentos': list(submomentos)})

def get_respuesta(request):
    submomento_id = request.GET.get('submomento_id')
    respuestas = Respuesta.objects.filter(submomento_id=submomento_id).values('id', 'contenido')
    return JsonResponse({'respuestas': list(respuestas)})

def get_historial(request):
    historial = Historial.objects.all().values(
        'momento__nombre', 'submomento__nombre', 'respuesta__contenido', 'timestamp'
    )
    return JsonResponse({'historial': list(historial)})

def nueva_conversacion(request):
    # Reinicia lógica de la conversación
    return JsonResponse({'status': 'Nueva conversación iniciada'})
