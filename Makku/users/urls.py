from django.urls import path, include
from . import views as views_user

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
#    path('card/<str:user_id>', views_user.user_card, name='user-name'),

]