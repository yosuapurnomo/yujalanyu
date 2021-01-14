from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import ( DetailPaket, SearchPaket)

app_name='paket'
urlpatterns = [
		re_path(r'^$', SearchPaket.as_view(query_string=False), name='view'),
		re_path(r'^search/', SearchPaket.as_view(query_string=True), name='search'),
		re_path(r'^detail/(?P<slug>[\w-]+)$', DetailPaket.as_view(), name='detail'),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'Travel.views.handle404'

# handler500 = 'Travel.views.handle404'