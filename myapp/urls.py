from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'myapp'

urlpatterns = [
	# path('', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
	path('upload_csv', views.upload_csv, name='uploadcsv'),
	path('upload', views.upload_csv_process, name='upload')
]

# path('admin/', admin.site.urls),