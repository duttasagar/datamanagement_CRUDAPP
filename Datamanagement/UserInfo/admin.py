from django.contrib import admin
from .models import Usermodel
# Register your models here.

class UsermodelAdmin(admin.ModelAdmin):
    list_display=("id" , "name" , "email" , "age")

admin.site.register(Usermodel , UsermodelAdmin)
