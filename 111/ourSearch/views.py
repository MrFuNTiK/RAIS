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
def results(request):
    urls = ""
    if request.method == 'POST':

        form = ParseForm(request.POST)

        #allWords = []
        if form.is_valid():
            word = form.cleaned_data['word']
            urls = find_word(word)
            #allWords.append(words)
            

    #return render(request, "ourSearch/results.html", {"count": count})
    return render(request, "ourSearch/results.html", locals())
    #return render(request, "ourSearch/results.html", {"text": text})
    #return render(request, "ourSearch/results.html", {"ourSites": ourSites})

def adminSite(request):
    ourSites = URLTable.objects.all()
    #urls = get_object_or_404(URLTable)
    if request.method == 'POST':

        form = URLForm(request.POST)

        if form.is_valid():
            #form.clean()
            url = form.cleaned_data['urladress']
            add_url(url)
            update_words(url)
            #return render(request, "ourSearch/adminSite.html", locals())


    return render(request, "ourSearch/adminSite.html", locals())

def index(request):

    return render(request, "ourSearch/index.html", locals())


#class OurUrlView(ListView):
   # model = OurUrl
    #template_name = 'ourSearch/index.html'
    #context_object_name = "ourUrls"
