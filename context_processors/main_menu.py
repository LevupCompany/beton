from django.template.context_processors import request

#Импортируем модель категорий
from catalog.models import City,Category,Subcategory,Tovar
from catalog.forms import *
def menu(request):
    category_list = Category.objects.all()
    city_list = City.objects.all()
    cookie = request.COOKIES.get('City_choise')
    if cookie is None:
        cookie='odessa'
    return {
                "category_list":category_list,
                "city_list":city_list,
                "city":cookie,
                "city_name":City.objects.get(slug=cookie).name
                }
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
            city_form = City.objects.get(slug=city)
            fs.city = city_form.name
            fs.is_all = True
            fs.save()
            return redirect('home')
    else:
        orderforms = CreateOrders()
    return {'cat':cat,'subcat':subcat,'tov':tov,'orderforms':orderforms}
