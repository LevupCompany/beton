from django.contrib import admin
from catalog.models import City,Category,Subcategory,Tovar,Order,Review

class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']          # в каких полях делать поиск в админке
# добавить модель Page в админку
admin.site.register(City, CityAdmin)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']          # в каких полях делать поиск в админке
# добавить модель Page в админку
admin.site.register(Category, CategoryAdmin)
class SubcategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']          # в каких полях делать поиск в админке
# добавить модель Page в админку
admin.site.register(Subcategory, SubcategoryAdmin)
# Register your models here.
class TovarAdmin(admin.ModelAdmin):
    search_fields = ['name']          # в каких полях делать поиск в админке
# добавить модель Page в админку
admin.site.register(Tovar, TovarAdmin)
class OrderAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','phone','item','vendor']
admin.site.register(Order,OrderAdmin)
class ReviewAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','range','order',]
admin.site.register(Review,ReviewAdmin)
#     search_fields = ['name']          # в каких полях делать поиск в админке
# # добавить модель Page в админку
# admin.site.register(TovarTag, TovarTagAdmin)
