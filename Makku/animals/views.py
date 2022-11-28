from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def registration_form_animal(request):
    context = {
        'registration_form_user': 'Форма регистрации животного html',

    }
    return render(request, 'animals/registration_form_animal.html', context=context)


def animal_card(request):
    context = {
        'animal_card': 'Карточка животного html',
    }
    return render(request, 'animals/animal_card.html', context=context)