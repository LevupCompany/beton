from django.contrib import admin
from blog.models import Post # импорт модели Page из файла pages/models.py

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published_date') # какие поля выводить в админке
    search_fields = ['title']          # в каких полях делать поиск в админке

# добавить модель Page в админку
admin.site.register(Post, PostAdmin)
# Register your models here.
