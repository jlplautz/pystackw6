from django.contrib import admin

from .models import Certificado, Evento

# Register your models here.
admin.site.register(Evento)
admin.site.register(Certificado)
