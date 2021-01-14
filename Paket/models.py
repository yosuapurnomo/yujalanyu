from django.db import models
from django.utils.text import slugify

# Create your models here.
class modelPaket(models.Model):
	nama_paket = models.CharField(max_length=100)
	destinasi = models.CharField(max_length=100)
	about = models.TextField()
	harga = models.IntegerField()
	lama_hari = models.IntegerField()
	tgl_berangkat = models.DateField()
	tgl_dibuat = models.DateField(auto_now=True, editable=False)
	slug = models.SlugField(editable=False)

	def save(self):
		self.slug = slugify(f"{self.nama_paket}")
		super().save()

	def __str__(self):
		return f"{self.id} - {self.nama_paket}"

class imagesPaket(models.Model):
	id_paket = models.ForeignKey('modelPaket',related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return f"{self.id} - {self.id_paket}"

	def getImage(self):
		return self.image.url

