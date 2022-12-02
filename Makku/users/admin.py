from django.contrib import admin
from .models import db_additional
from django.contrib.auth.models import User



class db_add_admin(admin.ModelAdmin):
    list_display = ['email', 'city', 'coordinate', 'IP', 'createOn', 'isactive', 'description']

admin.site.register(db_additional, db_add_admin)