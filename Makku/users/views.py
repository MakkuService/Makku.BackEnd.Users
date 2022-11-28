from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def registration_form_user(request):
    context = {
        'registration_form': 'Форма регистрации',

    }
    return render(request, 'users/registration_form_user.html', context=context)


def user_card(request, user_id:str):
    context = {
        'user_card': 'Карточка пользователя (лк)',
        'user_id': user_id,
    }
    return render(request, 'users/user_card.html', context=context)