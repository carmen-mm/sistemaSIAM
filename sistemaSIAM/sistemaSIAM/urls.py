"""sistemaSIAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path, include
# Acá están las urls globales y se incluyen las urls de cada aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beneficiario/', include('apps.beneficiario.urls')),
    path('ambulatorio/', include('apps.pedido_ambulatorio.urls')),
    path('doctores/', include('apps.doctores.urls')),
    path('centromedico/', include('apps.centromedico.urls')),
    path('internacion/', include('apps.solicitud_internacion.urls')),
    path('cirugia/', include('apps.solicitud_cirugia.urls')),
    path('novedades/', include('apps.novedades.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('', LoginView.as_view(template_name='login.html')),
    path('logout/', logout_then_login, name='logout'),

]
