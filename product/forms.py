from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import Tovar,Order
from .models import *

class CreateTovar(forms.ModelForm):
    name = forms.ModelChoiceField(label='Товар',widget=forms.Select(attrs={'class': 'col-md-7 custom-select yellow yellow11 rounded-0'}),queryset=Tovar.objects.all())
    detail = forms.CharField(label='Описание',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите ИНН'}))
    price = forms.IntegerField(label='Цена',widget=forms.NumberInput(attrs={'class': 'col-md-7 form-control rounded-0'}))
    class Meta:
        model = Product
        fields = ('name','detail','price')

class OrderCheck(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('check',)
class OrderChecks(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('cancel',)
