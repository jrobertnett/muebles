from django.contrib import admin
from .models import Cliente

# Register your models here.

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('dpi', 'nombre','apellidos', 'direccion', 'telefono'  )
	search_fields = ('dpi', 'nombre')
