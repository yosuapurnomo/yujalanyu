from django.db import models
from django.contrib.auth.models import User
from Paket.models import modelPaket

# Create your models here.
class modelTransaksi(models.Model):
	paket = models.ForeignKey(modelPaket, 
							on_delete=models.DO_NOTHING)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	jumlah = models.IntegerField()
	totalHarga = models.IntegerField()
	token = models.CharField(max_length=200)
	status = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.id}-{self.paket}"

