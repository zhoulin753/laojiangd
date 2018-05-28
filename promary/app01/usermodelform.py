from django.forms import ModelForm,Form,fields
from django import forms
from .models import *
# class myform(Form):
#     name = fields.CharField()
#     phone = fields.CharField()
#     password = fields.CharField()
#     email = fields.EmailField()

class Usermodelform(ModelForm):
    class Meta:
        model =Userinfo
        fields = '__all__'