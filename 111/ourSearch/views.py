from django.shortcuts import render
from .models import *
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .forms import *
from .get_text_MY import *
from .add_url import *
from .update_words import *
from .find_word import *
from .rm_url import *
def results(request):
    urls = ""
    if request.method == 'GET':
        form = ParseForm(request.GET)
        if form.is_valid():
            word = form.cleaned_data['word']
            urls = find_word(word)

    if request.method == 'POST':
        form = ParseForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            urls = find_word(word)

    return render(request, "ourSearch/results.html", locals())

def adminSite(request):
    ourSites = URLTable.objects.all()
    if request.method == 'POST':
        if 'update' in request.POST:
                update_words()

        form = URLForm(request.POST)
        if form.is_valid():
            #form.clean()
            url = form.cleaned_data['urladress']
            add_url(url)
            #return render(request, "ourSearch/results.html", locals())


    return render(request, "ourSearch/adminSite.html", locals())

def index(request):
    if request.method == 'GET':
        form = ParseForm(request.GET)
        if form.is_valid():
            word = form.cleaned_data['word']
            urls = find_word(word)
            return redirect('results', locals())

    return render(request, "ourSearch/index.html", locals())

def auth(request):

    return render(request, "ourSearch/auth.html", locals())
