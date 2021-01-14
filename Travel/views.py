from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from Paket.models import modelPaket, imagesPaket
import datetime

# def adminLog(request):
# 	if request.user.is_superuser:
# 		return HttpResponseRedirect(reverse('admin:index'))
# 	else: return redirect(reverse('home'))
def handle404(request, exception=None):
	return HttpResponseRedirect(reverse('home'))


class homeView(View):
	template_name = 'home.html'
	http_method_name = ['get']

	def get(self, request):
		model = modelPaket.objects.order_by('-tgl_dibuat')
		modelImg = imagesPaket.objects.all()

		dataPaket = []
		dataImg = []
		for x in model:
			if x.tgl_berangkat > datetime.date.today():
				dataPaket.append(x)
		
		for x in modelImg.values('id_paket').distinct():
			oper = modelImg.filter(id_paket=x['id_paket'])
			dataImg.append(oper[0])
				
		context = {
		'title':"HOME",
		'data':dataPaket,
		'img':dataImg
		}

		return render(self.request, self.template_name, context)