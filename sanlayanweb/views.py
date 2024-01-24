from urllib import response
from django.shortcuts import render, HttpResponse
from sanlayanweb.models import person, gallery1
import requests

# Create your views here.

def index (request):
   #return HttpResponse('this is homepage')
   return render (request, 'index.html')


def about (request):
   return render (request, 'about.html')

def services (request):
   return render (request, 'services.html')

def team (request):
   return render (request, 'team.html')

def gallery (request):
   gallery_con = gallery1.objects.all()
   
   data={
      'gallery_con':gallery_con,
   }
   
   print(gallery_con)
   return render (request, 'gallery.html', data)

def contact (request):
   return render (request, 'contact.html')