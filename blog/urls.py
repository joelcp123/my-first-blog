#Here we're importing Django's function url and all of our views from the blog application
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
