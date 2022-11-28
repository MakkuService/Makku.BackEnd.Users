from django.urls import path
from . import views as views_shelter

urlpatterns = [
    path('registration_form', views_shelter.registration_form_shelter),
    path('<str:shelter_id>', views_shelter.shelter_card, name='shelter-name'),
]