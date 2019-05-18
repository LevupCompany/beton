from django.shortcuts import render,get_object_or_404,redirect
from catalog.models import City,Category,Subcategory,Tovar,Count,Order,Review
from django.http import HttpResponse
from django.conf import settings
from product.models import Product
from felixuser.models import Profile
from django.db.models import F,Avg
from .forms import *

city_slug = City.slug
cat_slug = Category.slug
subcat_slug = Subcategory.slug
tovar_slug = Tovar.slug
cat_list = Category.objects.order_by('name')
subcat_list = Subcategory.objects.order_by('name')
tovar_list = Tovar.objects.order_by('name')
import datetime

def set_cookie(response, key, value, days_expire = 365):
  if days_expire is None:
    max_age = 365 * 24 * 60 * 60  #one year
  else:
    max_age = days_expire * 24 * 60 * 60
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)

def index(request):
    return render(request, "catalog/index.html", {"cat_list":cat_list,"subcat_list":subcat_list})
def company(request, pk):
    company = Profile.objects.get(id=pk)
    orders = Review.objects.filter(order__vendor=company.user)
    avg = orders.aggregate(average_range=Avg('range'))
    try:
        count = Count.objects.filter(profile=company.user)
    except Count.DoesNotExist:
        count = None
    cookie = request.COOKIES.get("%s"%(pk))
    if request.method == 'POST':
        orderform = CreateOrder(request.POST)
        if orderform.is_valid():
            fs = orderform.save()
            fs.refresh_from_db()
            city = request.COOKIES.get('City_choise')
            city_form = City.objects.get(slug=city)
            fs.city = city_form.name
            fs.vendor = company.user
            fs.save()
            return redirect('home')
        # reviewform = CreateReview(request.Post)
        #     if reviewform.is_valid():
        #         fs=reviewform.save()
        #         fs.refresh_from_db()
        #         order = Order.objects.filter(vendor=company.user)
        #         if fs.order in order.id:
        #             fs.order = reviewform.cleaned_data.get('order')
        #         else:
        #             reviewform.add_error('order', 'Заказ не найден')
        #         fs.save()
    else:
        orderform = CreateOrder()
    response = render(request, 'catalog/company.html', {'company':company, 'review':avg, 'rev':orders, 'count':count,'cookie':cookie,'orderform':orderform})
    if cookie is None:
        set_cookie(response, "%s"%(pk),value="visited")
        count.update(name=F("name") + 1)
    return response
def city(request, city_slug):
    cts = get_object_or_404(City, slug=city_slug)
    response = render(request, "catalog/index.html",{"cat_list":cat_list,"subcat_list":subcat_list})
    set_cookie(response, 'City_choise', value=cts.slug)
    return response
def category(request,city_slug,cat_slug):
    cathegory = get_object_or_404(Category, slug=cat_slug)
    subcat_list = Subcategory.objects.filter(category=cathegory.id).order_by('name')
    return render(request, "catalog/category.html",{"cath":cathegory,"cat_list":cat_list,"subcat_list":subcat_list,"cat_slug": cat_slug,"tovar_list":tovar_list})
def subcategory(request,city_slug,cat_slug,subcat_slug):
    cathegory = get_object_or_404(Category, slug=cat_slug)
    subcathegory = get_object_or_404(Subcategory, slug=subcat_slug)
    tovar = Tovar.objects.filter(category=subcathegory)
    product = Product.objects.order_by('price').select_related('company')
    orders = Review.objects.filter()
    avg = orders.aggregate(average_range=Avg('range'))
    if request.method == 'POST':
        orderform = CreateOrderr(request.POST)
        if orderform.is_valid():
            fs = orderform.save()
            fs.refresh_from_db()
            city = request.COOKIES.get('City_choise')
            city_form = City.objects.get(slug=city)
            fs.city = city_form.name
            fs.vendor = product
            fs.save()
            return redirect('home')
    else:
        orderform = CreateOrderr()
    return render(request, "catalog/subcategory.html", {"products":orders, "avg":avg, "tovar":tovar, "product":product,"cat_slug":cat_slug,"subcat_slug":subcat_slug,"orderform":orderform})
def tovar(request,city_slug,cat_slug,subcat_slug,tovar_slug):
    cathegory = get_object_or_404(Category, slug=cat_slug)
    subcathegory = get_object_or_404(Subcategory, slug=subcat_slug)
    tovar = Tovar.objects.filter(category=subcathegory)
    tovar_item=get_object_or_404(Tovar, slug=tovar_slug)
    product = Product.objects.filter(name=tovar_item)
    if request.method == 'POST':
        orderform = CreateOrderr(request.POST)
        if orderform.is_valid():
            fs = orderform.save()
            fs.refresh_from_db()
            city = request.COOKIES.get('City_choise')
            city_form = City.objects.get(slug=city)
            fs.city = city_form.name
            fs.vendor = product
            fs.save()
            return redirect('home')
    else:
        orderform = CreateOrderr()
    return render(request, "catalog/subcategory.html",{"tovar":tovar,"tovar_item":tovar_item, "product":product,"cat_slug":cat_slug,"subcat_slug":subcat_slug,"orderform":orderform})
