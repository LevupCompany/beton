from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from uuslug import slugify
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    text = HTMLField(verbose_name=u'Text')
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = '{0}'.format(slugify(self.title))  # Статья будет отображаться в виде NN-АА-АААА
        super(Post, self).save()
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    class Meta:
         verbose_name = "Новость"
         verbose_name_plural = "Новости"
