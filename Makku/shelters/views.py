from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def registration_form_shelter(request):
    context = {
        'registration_form_shelter': 'Форма приюта html',

    }
    return render(request, 'shelters/registration_form_shelter.html', context=context)


def shelter_card(request):
    context = {
        'shelter_card': 'Карточка приюта html',
    }
    return render(request, 'shelters/shelter_card.html', context=context)