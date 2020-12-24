from django.shortcuts import render
from .models import *
# Create your views here.
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
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


from django.contrib.auth.decorators import login_required

@login_required
def adminSite(request):
        if request.method == 'POST':
            if 'update' in request.POST:
                update_words()
            if 'logout' in request.POST:
                logout(request)
            if 'view' or 'delete' in request.POST:
                ourSites = URLTable.objects.all()
                delform = DeleteURLForm(request.POST)
                if delform.is_valid():
                    delurl = delform.cleaned_data['url']
                    rm_url(delurl)
            form = URLForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['urladress']
                add_url(url)
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('adminSite', )
    return render(request, "ourSearch/auth.html", locals())

