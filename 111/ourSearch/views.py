from django.shortcuts import render
from .models import *
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

def results(request):
    ourSites = OurUrl.objects.all()
    return render(request, "ourSearch/results.html", {"ourSites": ourSites})


def index(request):
    return render(request, "ourSearch/index.html", locals())


#class OurUrlView(ListView):
   # model = OurUrl
    #template_name = 'ourSearch/index.html'
    #context_object_name = "ourUrls"
