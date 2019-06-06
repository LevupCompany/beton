import os,random
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Tovar
from felixuser.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

def get_upload_path(instance,filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'static/gallery/{id}/{randomstring}{ext}'.format(id=instance.user.id, basename=basefilename,
                                                            randomstring=randomstr, ext=file_extension)
# Create your models here.
class Product(models.Model):
    name = models.ForeignKey(Tovar, on_delete = models.CASCADE, verbose_name='Товар')
    company = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор')
    price = models.PositiveIntegerField(verbose_name='Цена')
    detail = models.CharField(max_length=250, blank=True,verbose_name='Описание')
    def __str__(self):
        return self.company.user.username


    def get_absolute_url(self):
        return reverse('tovar_show', kwargs={'pk': self.pk})
    class Meta:
         verbose_name = "Товар"
         verbose_name_plural = "Товары"
class Gallery(models.Model):
    image = models.ImageField(verbose_name='Фото компании',upload_to=get_upload_path)
    company = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор')
    def __str__(self):
        return self.company.user.username
class Tariff(models.Model):
    c = [(1, "Бесплатный"), (2, "Базовый"), (3, "Расширенный")]
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    status = models.IntegerField(choices=c,default=1)
    def __str__(self):
        return self.user.user.username
    class Meta:
         verbose_name = "Тариф"
         verbose_name_plural = "Тарифы"

class Banner(models.Model):
    p=[(1, "Светлый"),(2,"Темный")]
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст на баннере', default='', max_length=150)
    image = models.ImageField(verbose_name='Акция',  upload_to='static/banner/{user}/')
    fon = models.IntegerField(verbose_name="Фон оформления",choices=p,default=1)
    def __str__(self):
        return self.user.company
    class Meta:
         verbose_name = "Баннер"
         verbose_name_plural = "Баннера"
