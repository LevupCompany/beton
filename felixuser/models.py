from django.db import models
from django.db.models import F,Avg
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.context_processors import request
from catalog.models import City,Category,Order,Review
def get_upload_path(instance,filename):
    return 'static/avatars/{id}/{file}'.format(id=instance.user.id, file=filename)
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
    image = models.ImageField(verbose_name='Фото менеджера', blank=True,upload_to=get_upload_path)
    admin = models.CharField(max_length=200, blank=False, default='', verbose_name='Имя администратора')
    phone = models.CharField(max_length=12,blank=True, verbose_name='Номер менеджера')
    regions = models.ManyToManyField(City, verbose_name='Регионы доставки')
    def __str__(self):
        return self.user.username
    def rating(self):
        return Review.objects.filter(order__vendor=self.user).aggregate(average_range=Avg('range'))

    class Meta:
         verbose_name = "Профиль"
         verbose_name_plural = "Профили"
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
