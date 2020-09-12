from django.contrib import admin
from apps.solicitud_cirugia.models import Cirugia, Solicitud_Cirugia

# Register your models here.
admin.site.register(Cirugia)
admin.site.register(Solicitud_Cirugia)