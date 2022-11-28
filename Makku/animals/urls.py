from django.urls import path
from . import views as views_animal

urlpatterns = [
    path('registration_form', views_animal.registration_form_animal),
    path('<str:animal_id>', views_animal.animal_card, name='animal-name'),
]