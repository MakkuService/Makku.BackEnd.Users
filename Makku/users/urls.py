from django.urls import path
from . import views as views_user

urlpatterns = [
    path('registration_form', views_user.registration_form_user),
    path('card/<str:user_id>', views_user.user_card, name='user-name'),
]