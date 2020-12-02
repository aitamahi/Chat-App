from django.conf.urls import url
from .views import *
urlpatterns=[
	url(r'^home/',home_view,name='home_view'),
]	
