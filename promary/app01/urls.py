from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^use/$',views.use),
    url(r'^login/',views.log_in)
]