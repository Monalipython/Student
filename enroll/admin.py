from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
    
admin.site.register(Profile,ProfileAdmin)