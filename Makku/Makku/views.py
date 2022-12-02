from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def index(request):
    context = {
        'main': 'main',
    }
    return render(request, 'Makku/index.html', context=context)