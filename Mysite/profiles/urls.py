from django.urls import path
from django.conf.urls import url
from .views import *

app_name='profiles'
urlpatterns=[
	url(r'^myprofiles/',my_profile_view,name='my_profile_view')
]