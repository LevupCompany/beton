from django import forms
from django.contrib.auth.models import User
from .models import City, Category,Tovar,Order, Review
from felixuser.models import Profile
class CreateOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name','phone','detail','email','adress','item','weight','is_all')
class CreateOrderr(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name','phone','detail','email','adress','item','weight','is_all','vendor')
class CreateOrders(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name','phone','detail','email','adress','item','weight')
# class CreateReview(forms.ModelForm):
#     range = forms.Number
#     class Meta:
#         model = Review
#         fields = ('name','order','detail', 'range')
