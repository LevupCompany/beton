from django.db import models
from django.db.models import F,Avg
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from catalog.models import Count
from django_resized import ResizedImageField
from datetime import datetime

import sys,os,random
from django.template.context_processors import request
from catalog.models import City,Category,Order,Review
def get_upload_path(instance,filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'static/avatars/{id}/{randomstring}{ext}'.format(id=instance.user.id,basename=basefilename,randomstring=randomstr, ext=file_extension)
def get_upload_path2(instance,filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'static/logo/{id}/{randomstring}{ext}'.format(id=instance.user.id, basename=basefilename,
                                                                randomstring=randomstr, ext=file_extension)
class Notification(models.Model):
    text = models.TextField(max_length=500)
    date = datetime.now()
    def __str__(self):
        return self.text
    class Meta:
         verbose_name = "Уведомление"
         verbose_name_plural = "Уведомления"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.TextField(max_length=500, blank=False, verbose_name='Название компании')
    identificate = models.CharField(max_length=10, blank=False, verbose_name='ИНН')
    specialisation = models.ManyToManyField(Category,verbose_name='Основной вид дейтельности')
    director = models.TextField(max_length=500, blank=False,default='', verbose_name='Директор')
    city = models.CharField(max_length=200, default='Одесса',verbose_name='Город')
    street = models.CharField(max_length=200, default='Улица',verbose_name='Адрес офиса')
    street2 = models.CharField(max_length=200, blank=True, verbose_name='Адрес склада')
    site = models.URLField(verbose_name='Адрес сайта',blank=True)
    manager = models.TextField(max_length=200, blank=False,default='', verbose_name='Имя менеджера')
    image = ResizedImageField(size=[150, 150], crop=['middle', 'center'],verbose_name='Фото менеджера', blank=True,upload_to=get_upload_path)
    logo = ResizedImageField(size=[150, 150], crop=['middle', 'center'],verbose_name='Лого компании', blank=True,upload_to=get_upload_path2)
    admin = models.CharField(max_length=200, blank=False, default='', verbose_name='Имя администратора')
    phone = models.CharField(max_length=12,blank=True, verbose_name='Номер менеджера')
    regions = models.ManyToManyField(City, verbose_name='Регионы доставки')
    read = models.ManyToManyField(Notification, related_name='zones', null=False, blank=True)
    def __str__(self):
        return self.user.username
    def rating(self):
        return Review.objects.filter(order__vendor=self.user).aggregate(average_range=Avg('range'))
    # def special(self):
    #     return self.specialisation

    class Meta:
         verbose_name = "Профиль"
         verbose_name_plural = "Профили"
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
class SmsVerify(models.Model):
    number = models.CharField(blank=True, max_length=40,verbose_name='Номер менеджера')
    code = models.IntegerField(verbose_name='Проверочный код')
    class Meta:
        verbose_name = "Проверочный код"
        verbose_name_plural = "Проверочные коды"
