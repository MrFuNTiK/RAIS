from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('results/', views.results, name='results'),
    path('adminSite/', views.adminSite, name='adminSite'),
    url(r'^results/$', views.results, name='results'),
]