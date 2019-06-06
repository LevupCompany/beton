from django.shortcuts import render,get_object_or_404,redirect
from catalog.models import *
from django.http import HttpResponse
from django.conf import settings
from product.models import *
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
    subcat_list = Product.objects.select_related('name__category__category')
    sales = Banner.objects.filter(user__regions__slug=request.COOKIES.get('City_choise')).order_by('?')[:2]
    return render(request, "catalog/index.html", {"cat_list":cat_list,"subcat_list":subcat_list,"sales":sales})
def company(request, pk):
    company = Profile.objects.get(id=pk)
    orders = Review.objects.filter(order__vendor=company.user)
    avg = orders.aggregate(average_range=Avg('range'))
    tar = Tariff.objects.get(user=company)
    photo = Gallery.objects.filter(company=company)
    sales = Banner.objects.filter(user__regions__slug=request.COOKIES.get('City_choise')).order_by('?')[:2]

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
    response = render(request, 'catalog/company.html', {'company':company, 'review':avg, 'rev':orders, 'count':count,'cookie':cookie,'orderform':orderform,'tar':tar,'photo':photo,"sales":sales})
    if cookie is None:
        set_cookie(response, "%s"%(pk),value="visited")
        count.update(name=F("name") + 1)
    return response
def city(request, city_slug):
    cts = get_object_or_404(City, slug=city_slug)
    response = redirect('home')
    sales = Banner.objects.filter(user__regions__slug=request.COOKIES.get('City_choise')).order_by('?')[:2]
    set_cookie(response, 'City_choise', value=cts.slug)
    return response
def category(request,city_slug,cat_slug):
    tovar_list = Product.objects.select_related('name__category')
    sales = Banner.objects.filter(user__regions__slug=request.COOKIES.get('City_choise')).order_by('?')[:2]
    cathegory = get_object_or_404(Category, slug=cat_slug)
    subcat_list = Subcategory.objects.filter(category=cathegory.id).order_by('name')
    return render(request, "catalog/category.html",{"cath":cathegory,"cat_list":cat_list,"subcat_list":subcat_list,"cat_slug": cat_slug,"tovar_list":tovar_list,"sales":sales})
def subcategory(request,city_slug,cat_slug,subcat_slug):
    cathegory = get_object_or_404(Category, slug=cat_slug)
    subcathegory = get_object_or_404(Subcategory, slug=subcat_slug)
    tovar = Tovar.objects.filter(category=subcathegory)
    sales = Banner.objects.filter(user__regions__slug=request.COOKIES.get('City_choise')).order_by('?')[:2]
    product = Product.objects.order_by('price').select_related('company','company__tariff').exclude(company__tariff__status=1).filter(company__regions__slug=city_slug)
    orders = Review.objects.filter()
    avg = orders.aggregate(average_range=Avg('range'))
    if request.method == 'POST':
        orderform = CreateOrderr(request.POST)
        if orderform.is_valid():
            fs = orderform.save()
            fs.refresh_from_db()
            city = request.COOKIES.get('City_choise')
            city_form = City.objects.get(slug=city).name
            fs.city = city_form
            fs.vendor = product.company
            fs.save()
            return redirect('home')
    else:
        orderform = CreateOrderr()
    return render(request, "catalog/subcategory.html", {"cts":cathegory,"subcathegory":subcathegory,"products":orders, "avg":avg, "tovar":tovar, "product":product,"cat_slug":cat_slug,"subcat_slug":subcat_slug,"orderform":orderform,"sales":sales})
def tovar(request,city_slug,cat_slug,subcat_slug,tovar_slug):
    cathegory = get_object_or_404(Category, slug=cat_slug)
    subcathegory = get_object_or_404(Subcategory, slug=subcat_slug)
    tovar = Tovar.objects.filter(category=subcathegory)
    sales = Banner.objects.filter(user__regions__slug=request.COOKIES.get('City_choise')).order_by('?')[:2]
    tovar_item=get_object_or_404(Tovar, slug=tovar_slug)
    product = Product.objects.order_by('price').select_related('company','company__tariff').filter(name=tovar_item).exclude(company__tariff__status=1).filter(company__regions__slug=city_slug)
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
    return render(request, "catalog/subcategory.html",{"cts":cathegory,"subcathegory":subcathegory,"tovar":tovar,"tovar_item":tovar_item, "product":product,"cat_slug":cat_slug,"subcat_slug":subcat_slug,"orderform":orderform,"sales":sales})
def search(request):
    l = request.COOKIES.get('City_choise')
    l_2 = City.objects.get(slug=l)
    city = request.GET.get('city',l_2)
    if request.GET.get('city') =='':
        city =l_2
    tovar = request.GET.get('tovar', 1)
    city_url = City.objects.get(name=city)
    tovar_url = Tovar.objects.get(id=tovar)
    subcat_url = Subcategory.objects.get(name=tovar_url.category)
    cat_url = Category.objects.get(name=subcat_url.category)
    return redirect('catalog_tovar', city_slug=city_url.slug,cat_slug=cat_url.slug,subcat_slug=subcat_url.slug,tovar_slug=tovar_url.slug)
