from django.template.context_processors import request

#Импортируем модель категорий
from catalog.models import City,Category,Subcategory,Tovar
from catalog.forms import *
from felixuser.models import Notification
def menu(request):
    category_list = Category.objects.all()
    city_list = City.objects.all()
    cookie = request.COOKIES.get('City_choise')
    if cookie is None:
        cookie='odessa'
    if category_list:
        return {
                "category_list":category_list,
                "city_list":city_list,
                "city":cookie,
                "city_name":City.objects.get(slug=cookie).name
                }
    else:
        return
def order(request):
    cat = Category.objects.order_by('name')
    subcat = Subcategory.objects.order_by('category', 'name')
    tov = Tovar.objects.order_by('category','name')

    if request.method == 'POST':
        orderforms = CreateOrders(request.POST)
        if orderforms.is_valid():
            fs = orderforms.save()
            fs.refresh_from_db()
            city = request.COOKIES.get('City_choise')
            city_form = City.objects.get(slug=city).name
            fs.city = city_form
            fs.is_all = True
            fs.save()
            return redirect('home')
    else:
        orderforms = CreateOrders()
    return {'cat':cat,'subcat':subcat,'tov':tov,'orderforms':orderforms}
def notify(request):
    note = ''
    if request.user.is_authenticated:
        note = Notification.objects.exclude(zones=request.user.profile).count()
        if note == 0:
            note is None
    return {'note':note}
