from django.contrib import admin
from felixuser.models import Profile
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','company','identificate') # какие поля выводить в админке
# в каких полях делать поиск в админке
# добавить модель Page в админку
admin.site.register(Profile, UserAdmin)
# Register your models here.
