from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import Tovar,Order
from .models import *



class CreateTovar(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CreateTovar, self).clean()

        price = cleaned_data.get('price')
        name = cleaned_data.get('name')
        tovar = Tovar.objects.get(name=name)

        if price < tovar.min_price:
            raise forms.ValidationError("Минимальная цена товара %s" % tovar.min_price)
        return cleaned_data
    name = forms.ModelChoiceField(label='Товар',widget=forms.Select(attrs={'class': 'custom-select yellow4 yellow11 rounded-0'}),queryset=Tovar.objects.all())
    detail = forms.CharField(label='Описание',widget=forms.TextInput(attrs={'class': 'form-control rounded-0','placeholder':'Введите ИНН'}))
    price = forms.IntegerField(label='Цена',widget=forms.NumberInput(attrs={'class': 'form-control rounded-0'}))
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
class CreateGallery(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image',)

