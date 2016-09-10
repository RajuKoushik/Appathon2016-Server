from django.conf.urls import url
from . import views, views_feed

urlpatterns = [

    url(r'^register', views.register),
    url(r'^login', views.login),



]