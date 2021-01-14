from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.db.models import Q
from .models import modelPaket, imagesPaket
from Transaksi.models import modelTransaksi
from Transaksi.form import TransaksiForm
import datetime


# Create your views here.

class SearchPaket(ListView):
    model = modelPaket
    template_name = 'paket/viewPaket.html'
    context_object_name = 'paket_object'
    extra_context = {
        'title': 'PAKET LIST',
    }
    query_string = None

    def findSeacrh(self):
        url = self.request.GET.get('search', False)
        if url != False:
            dataPaket = []
            self.queryset = self.model.objects.filter(
                Q(nama_paket__icontains=self.request.GET['search']) |
                Q(destinasi__icontains=self.request.GET['search'])
            )
            for x in self.queryset:
                if x.tgl_berangkat > datetime.date.today():
                    print(x.tgl_berangkat)
                    dataPaket.append(x)
                print(len(dataPaket))
            if len(dataPaket) == 0:
                self.extra_context = {
                    'title': 'PAKET LIST',
                    'error': "Data Tidak diTemukan"
                }
                self.queryset = None
                return self.queryset
            else:
                return dataPaket
        else:
            self.query_string = False

    def get_queryset(self):
        if self.query_string:
            data = self.findSeacrh()
            return data
        else:
            dataPaket = []
            for x in self.model.objects.all():
                if x.tgl_berangkat > datetime.date.today():
                    dataPaket.append(x)
            return dataPaket;

    def get(self, *args, **kwargs):
        if self.query_string:
            if self.request.GET.get('search', False) is False:
                return HttpResponseRedirect(reverse('paket:view'))
        return super().get(self.request, *args, **kwargs)


class DetailPaket(FormMixin, DetailView):
    form_class = TransaksiForm
    model = modelPaket
    initial={}
    template_name = 'paket/detailPaket.html'
    extra_context = {
        'title': 'DETAIL',
    }

    def get_initial(self):
        dataPaket = self.model.objects.get(slug=self.kwargs['slug'])
        
        if self.request.user.is_authenticated:
            self.initial={
            'paket':dataPaket.slug,
            'user':self.request.user.email
            }
            return self.initial.copy()
        else:
            return super().get_initial()
