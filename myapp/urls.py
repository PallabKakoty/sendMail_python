from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'myapp'

urlpatterns = [
	# path('', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	path('upload_csv', views.upload_csv, name='uploadcsv'),
	path('upload', views.upload_csv_process, name='upload')
]