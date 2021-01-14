from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from .views import homeView

urlpatterns = [
    # path('admin/', adminLog),
    path('admin/', admin.site.urls, name='admin'),
    path('', homeView.as_view(), name='home'),
    path('', include('userManage.urls', namespace='akun')),
	path('paket/', include('Paket.urls', namespace='paket')),
	path('checkOut/', include('Transaksi.urls', namespace='transaksi')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Travel.views.handle404'

handler500 = 'Travel.views.handle404'