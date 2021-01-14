from django.contrib import admin
from .models import modelTransaksi

# Register your models here.
class adminTransaksi(admin.ModelAdmin):
	model = modelTransaksi
	readonly_fields = ['token', 'status']


admin.site.register(modelTransaksi, adminTransaksi)