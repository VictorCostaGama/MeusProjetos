from django.shortcuts import render
from django.http import HttpResponse
from .models import filme
from django.template import loader

# Create your views here.
def home(request):
    filme_all = filme.objects.all()
    template = loader.get_template('cineted/html/home.html')
    context = {
        'filme_all':filme_all,
    }

    return HttpResponse(template.render(context, request))


def detalhes(request, filme_title):
    return HttpResponse('<h3>' + filme_title.replace('-', ' ').title() + '</h3>')