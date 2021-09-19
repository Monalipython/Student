from django import forms
from django.db import models
from django.forms import fields, widgets
from django.forms.fields import Field
from django.forms.forms import Form
from .models import Profile ,Book

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':"Enter Name Here"}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter Email Here"}),
            'password' : forms.PasswordInput(render_value = True , attrs={'class':'form-control','placeholder':"Enter Password Here"}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')
