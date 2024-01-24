from django.contrib import admin
from django.urls import path, include
from sanlayanweb import views




urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    # path('services', views.services, name='services'),
    # path('contact', views.contact, name='contact'),
    # path('team', views.team, name='team'),
    # path('ourproduct', views.ourproduct, name='ourproduct'),
    # path('ourbusinessmodel', views.ourbusinessmodel, name='ourbusinessmodel'),
    # path('ouroperationalmodel', views.ouroperationalmodel, name='ouroperationalmodel'),
    # path('gallery', views.gallery, name='gallery'),
    # path('downloads', views.downloads, name='downloads'),
]