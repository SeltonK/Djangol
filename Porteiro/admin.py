from django.contrib import admin
from .models import Porteiro

class PorteiroAdmin(admin.ModelAdmin):
	list_display = ('image','nome','cpf','rg')
	list_filter = ('cidade','bairro','turno')
	search_fields = ['nome']
admin.site.register(Porteiro,PorteiroAdmin)
