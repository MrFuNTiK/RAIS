from django.shortcuts import render
from .models import *
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .forms import *
from .get_text_MY import *

def results(request):
    counts = COUNTTable.objects.all
    #count = counts.idurl
    ourSites = URLTable.objects.all()
    allWords = []
    for ourSite in ourSites:
        site = ourSite.urladress
        text = text_from_url(site)

        text = text.lower()
        text = remove_spec_signs(text)
        text = text.replace(' ', '\n')
        text = remove_short_words(text)
        text = remove_empty_strings(text)

        words = count_words(text)
        allWords.append(words)
    #ourSites = URLTable.objects.all()

    #return render(request, "ourSearch/results.html", {"count": count})
    return render(request, "ourSearch/results.html", {"words": allWords})
    #return render(request, "ourSearch/results.html", {"text": text})
    #return render(request, "ourSearch/results.html", {"ourSites": ourSites})

def adminSite(request):
    ourSites = URLTable.objects.all()
    #urls = get_object_or_404(URLTable)
    if request.method == 'POST':

        form = URLForm(request.POST)

        if form.is_valid():
            form.save()
            #return render(request, "ourSearch/adminSite.html", locals())
        #все что к form2 - пока не работает
        form2 = ParseForm(request.POST)
        if form2.is_valid():
            allWords = []
            for ourSite in ourSites:
                site = ourSite.urladress
                text = text_from_url(site)
                text = text.lower()
                text = remove_spec_signs(text)
                text = text.replace(' ', '\n')
                text = remove_short_words(text)
                text = remove_empty_strings(text)
                words = count_words(text)
                allWords.append(words)

            form2.save()

    return render(request, "ourSearch/adminSite.html", locals())

def index(request):
    return render(request, "ourSearch/index.html", locals())


#class OurUrlView(ListView):
   # model = OurUrl
    #template_name = 'ourSearch/index.html'
    #context_object_name = "ourUrls"
