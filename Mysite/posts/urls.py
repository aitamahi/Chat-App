from django.conf.urls import url
from .views import *
urlpatterns=[
	url(r'^postcomment/',post_commeent_create_and_list_view,name="main-post-view"),
	url(r'^liked/',like_unlike_post,name='like-post-view'),
	]