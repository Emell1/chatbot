"""
URL configuration for chatbot_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView  # Importamos TemplateView para servir HTML estático
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="Index.html"), name='index'),  # Página principal
    path('get-tipo-lead/', views.get_tipo_lead, name='get_tipo_lead'),
    path('get-programa/', views.get_programa, name='get_programa'),
    path('get-momento/', views.get_momento, name='get_momento'),
    path('get-submomento/', views.get_submomento, name='get_submomento'),
    path('get-historial/', views.get_historial, name='get_historial'),
    path('nueva-conversacion/', views.nueva_conversacion, name='nueva_conversacion'),
]
