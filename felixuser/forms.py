from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import City, Category
from .models import Profile
class SignUpForm(UserCreationForm):
    company = forms.CharField(label='Компания',help_text='Обязательное поле',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя компании'}))
    identificate = forms.CharField(label='ИНН',help_text='10 цифр',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите ИНН'}))
    specialisation = forms.ModelMultipleChoiceField(label='Виды специализации',widget=forms.SelectMultiple(attrs={'class': 'col-md-7 custom-select yellow yellow11 rounded-0'}),queryset=Category.objects.all())
    city = forms.CharField(label='Город',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите город'}))
    director = forms.CharField(label='Директор',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя директора'}))
    site = forms.URLField(label='Сайт',required=False,widget=forms.URLInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Скопируйте ссылку на сайт'}))
    manager = forms.CharField(label='Имя менеджера',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя менеджера'}))
    image = forms.ImageField(label='Фото менеджера',required=False,widget=forms.FileInput(attrs={'class': 'col-md-7 form-control-file rounded-0','placeholder':'Введите имя директора'}))
    admin = forms.CharField(label='ФИО администратора',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите ФИО администратора'}))
    username = forms.CharField(label='Номер администратора',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите Номер администратора'}))
    street = forms.CharField(label='Адрес офиса',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите адрес офиса'}))
    street2 = forms.CharField(label='Адрес склада',required=False,widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите адрес склада'}))
    password1 = forms.CharField(label="Пароль",strip=False,widget=forms.PasswordInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите пароль'}),)
    password2 = forms.CharField(label="Подтверждение пароля",strip=False,widget=forms.PasswordInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите пароль ещё раз'}),)
    phone = forms.CharField(label='Номер менеджера',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите номер менеджера'}))
    regions = forms.ModelMultipleChoiceField(label='Регионы поставки',widget=forms.SelectMultiple(attrs={'class': 'col-md-7 custom-select yellow yellow11 rounded-0'}), queryset=City.objects.all())
    class Meta:
        model = User
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'col-md-7 form-control rounded-0'}),
            'password2': forms.PasswordInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите почту'}),
        }
        fields = ('username', 'company',  'director', 'site', 'manager', 'image', 'admin', 'email', 'identificate', 'password1', 'password2', )
class EditProfile(forms.ModelForm):
    company = forms.CharField(label='Компания',help_text='Обязательное поле',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя компании'}))
    identificate = forms.CharField(label='ИНН',help_text='10 цифр',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите ИНН'}))
    city = forms.CharField(label='Город',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите город'}))
    director = forms.CharField(label='Директор',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя директора'}))
    site = forms.URLField(label='Сайт',required=False,widget=forms.URLInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Скопируйте ссылку на сайт'}))
    manager = forms.CharField(label='Имя менеджера',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите имя менеджера'}))
    image = forms.ImageField(label='Фото менеджера',required=False,widget=forms.FileInput(attrs={'class': 'col-md-7 form-control-file rounded-0','placeholder':'Введите имя директора'}))
    admin = forms.CharField(label='ФИО администратора',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите ФИО администратора'}))
    street = forms.CharField(label='Адрес офиса',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите адрес офиса'}))
    street2 = forms.CharField(label='Адрес склада',required=False,widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите адрес склада'}))
    phone = forms.CharField(label='Номер менеджера',widget=forms.TextInput(attrs={'class': 'col-md-7 form-control rounded-0','placeholder':'Введите номер менеджера'}))
    class Meta:
        model = Profile
        fields = ( 'company', 'city', 'director', 'site', 'manager', 'image', 'admin','identificate', 'street', 'street2', 'phone')
class EditRegions(forms.ModelForm):
    regions = forms.ModelMultipleChoiceField(label='Регионы поставки',widget=forms.SelectMultiple(attrs={'class': 'col-md-7 custom-select yellow yellow11 rounded-0'}), queryset=City.objects.all())
    class Meta:
        model = Profile
        fields = ( 'regions', )
class EditSpec(forms.ModelForm):
    specialisation = forms.ModelMultipleChoiceField(label='Виды специализации',widget=forms.SelectMultiple(attrs={'class': 'col-md-7 custom-select yellow yellow11 rounded-0'}),queryset=Category.objects.all())
    class Meta:
        model = Profile
        fields = ( 'specialisation', )
