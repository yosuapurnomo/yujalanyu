from django.contrib import admin
from .models import modelPaket, imagesPaket

# Register your models here.

class adminPaket(admin.ModelAdmin):
	model = [modelPaket, imagesPaket]
	readonly_fields = ['slug', 'tgl_dibuat',]

admin.site.register(imagesPaket)
admin.site.register(modelPaket, adminPaket)