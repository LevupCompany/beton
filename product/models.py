from django.db import models
from django.contrib.auth.models import User
from catalog.models import Tovar
from felixuser.models import Profile

# Create your models here.
class Product(models.Model):
    name = models.ForeignKey(Tovar, on_delete = models.CASCADE, verbose_name='Товар')
    company = models.ForeignKey(Profile, on_delete = models.CASCADE, verbose_name='Автор')
    price = models.PositiveIntegerField(verbose_name='Цена')
    detail = models.CharField(max_length=250, blank=True,verbose_name='Описание')
    def __str__(self):
        return self.company.user.username
    def get_absolute_url(self):
        return reverse('tovar_show', kwargs={'pk': self.pk})
    class Meta:
         verbose_name = "Товар"
         verbose_name_plural = "Товары"
