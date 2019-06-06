from django.db import models
from django.db.models import F,Avg,Min
from uuslug import slugify
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
class City(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def save(self):
        self.slug = '{0}'.format(slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
        super(City, self).save()
    class Meta:
         verbose_name = "Город"
         verbose_name_plural = "Города"
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(verbose_name='Иконка', blank=True, upload_to='static/images')
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)
    cities = models.ManyToManyField(City)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def save(self):
        self.slug = '{0}'.format(slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
        super(Category, self).save()
    class Meta:
         verbose_name = "Категория"
         verbose_name_plural = "Категории"
class Subcategory(models.Model):
    c = [('м<sup><small>3</small></sup>', "Кубометр"), ('шт.', "Штук"), ('т.', "Тонна")]
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)
    weight = models.CharField(max_length=250,choices=c, default='шт.')
    image = models.ImageField(verbose_name='Иконка',upload_to='static/images')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='Категория')
    def __str__(self):
        return self.name
    def minimus(self):
        return Tovar.objects.filter(category=self).aggregate(average_price=Min('product__price'))
    def __unicode__(self):
        return self.name
    def save(self):
        self.slug = '{0}'.format(slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
        super(Subcategory, self).save()
    class Meta:
         verbose_name = "Подкатегория"
         verbose_name_plural = "Подкатегории"
class Tovar(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)
    category = models.ForeignKey(Subcategory, on_delete = models.CASCADE, verbose_name='Категория')
    min_price = models.IntegerField(verbose_name ='Минимальная цена', default=100)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def minimus(self):
        return Tovar.objects.filter(name=self.name).aggregate(average_price=Min('product__price'))
    def save(self):
        self.slug = '{0}'.format(slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
        super(Tovar, self).save()
    class Meta:
         verbose_name = "Товар"
         verbose_name_plural = "Товары"
class Count(models.Model):
    name = models.BigIntegerField(default='0', verbose_name='Просмотры')
    profile = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='Компания')
    def __str__(self):
        return self.name
class Order(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя пользователя')
    detail = models.TextField(default='',verbose_name='Детали заказа')
    phone = models.CharField(max_length=12, verbose_name='Номер пользователя')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    city = models.CharField(max_length=200, default='Одесса',verbose_name='Город')
    adress = models.CharField(max_length=200,verbose_name='Адрес доставки')
    item = models.ForeignKey(Tovar, on_delete = models.CASCADE, verbose_name='Товар')
    weight = models.IntegerField(blank=True,verbose_name='Объем')
    is_all = models.BooleanField(default=False,verbose_name='Отправить для всех получателей')
    vendor = models.ForeignKey(User, on_delete = models.CASCADE, null=True,blank=True, verbose_name='Производитель')
    date = models.DateTimeField(default=datetime.now)
    check = models.BooleanField(default=False,verbose_name='Выполнен')
    cancel = models.BooleanField(default=False,verbose_name='Отменен')
    def __str__(self):
        return u'%s(%s)' % (self.name, self.id)
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
class Review(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя пользователя')
    order = models.OneToOneField(Order,default='', on_delete = models.CASCADE, verbose_name='Заказ',primary_key = True)
    detail = models.TextField(default='',verbose_name='Текст отзыва')
    range = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],verbose_name='Оценка')
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

# class TovarTag(models.Model):
#     name = models.CharField(max_length=250, verbose_name='Название')
#     slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)
#     tovar = models.ForeignKey(Tovar, on_delete = models.CASCADE, verbose_name='Товар')
#     def __str__(self):
#         return self.name
#     def __unicode__(self):
#         return self.name
#     def save(self):
#         self.slug = '{0}'.format(slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
#         super(TovarTag, self).save()

    # Поле для записи ссылки
# Create your models here.
