from django.contrib import admin

from apps.doctores.models import Especialidad, Doctor, DoctorTieneEspecialidad

# Register your models here.
admin.site.register(Especialidad)
admin.site.register(Doctor)
admin.site.register(DoctorTieneEspecialidad)