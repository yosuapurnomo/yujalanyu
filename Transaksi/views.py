import midtransclient

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse
from .models import modelTransaksi
from django.contrib.auth.models import User
from Paket.models import modelPaket
from .form import TransaksiForm


# Create your views here.

class checkOut(CreateView):
	model = modelTransaksi
	form_class = TransaksiForm
	query_string = True
	http_method_names = ['post']

	# def get(self, request):
	# 	return HttpResponseRedirect(reverse('paket:view'))

	def post(self, request):
		paket = modelPaket.objects.get(slug=request.POST['paket'])
		user = User.objects.get(email=request.POST['user'])
		snap = midtransclient.Snap(
		is_production=False,
		server_key='SB-Mid-server-uoBpcWvYMzSk72FbVUEUcPox',
		client_key='SB-Mid-client-EOjbQuFJwheGValW')

		jumlah = int(request.POST['jumlah'])
		param = {
			"transaction_details": {
				"order_id": f"order-{request.POST['csrfmiddlewaretoken'][0:5]}",
				"gross_amount": (jumlah * paket.harga),
				"customer_email": user.email
			},
			"enabled_payments": [ "bca_klikbca", "bca_klikpay", "bca_va", "bni_va", "gopay", "indomaret"],
			"credit_card": {
				"secure": True,
				"bca_va": {
	        	"free_text": {
	            "inquiry": [
	                {
	                    "id": "Silakan Selesaikan Transaksi Anda"
	                }
	            ],
	            "payment": [
	                {
	                    "id": "Pembayaran"
	                }
	            ]
	        }
},
			}}
		token = snap.create_transaction(param)

		data = self.form_class({'paket': paket, 'user': user, 'jumlah': jumlah,
								'totalHarga': (jumlah * paket.harga), 'token': token['token'], 'status': 'pendding'})
		data.save()
		return HttpResponseRedirect("%s?token={}".format(data['token'].data) % (reverse('transaksi:final')))
		
class DetailCheckOut(DetailView):
	model = modelTransaksi
	template_name = 'transaksi/checkOut_Final.html'
	query_string = True
	extra_context = {
	'status':"Yuk! Tinggal Satu Langkah Lagi",
	'body': "Kamu dapat menikmati perjalanan yang kamu impikan"
	}

	def get_object(self):
		try:
			self.queryset = get_object_or_404(self.model, token=self.request.GET.get('token'))
		except Exception as e:
			self.queryset = None
			self.extra_context = {
			'status':"Maaf Transaksi Ini Tidak Ada"
			}
		return self.queryset

	def get(self, *args, **kwargs):
		if self.request.GET.get('token', False) == False:
			return HttpResponseRedirect(reverse('paket:view'))

		data = self.model.objects.filter(token=self.request.GET.get('token')).first()
		if data != None:
			if data.status == 'success':
				return HttpResponseRedirect("%s?token={}".format(data.token) % (reverse('transaksi:success')))

		return super().get(args, kwargs)
			
class DetailSuccess(ListView):
	model = modelTransaksi
	template_name = 'transaksi/checkOut_success.html'
	query_string = True

	def get(self, *args, **kwargs):
		token = self.request.GET.get('token', False)
		try:
			trans = self.model.objects.get(token=token)
			trans.status = 'success'
			trans.save()
		except Exception as e:
			return HttpResponseRedirect(reverse('paket:view'))

		return super().get(args, kwargs)
