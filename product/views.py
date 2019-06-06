from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Avg
from django.contrib.auth.models import User
from catalog.models import *
import datetime
from qsstats import QuerySetStats
from datetime import *
from dateutil.relativedelta import *
import calendar
@login_required()
def index_tovar(request):
    tovar_list = Product.objects.filter(company=request.user.id)
    spec = request.user.profile.specialisation
    return render(request,'product/tovar.html', {'tovar_list':tovar_list,'spec':spec})
def cat_tovar(request, pk):
    tovar_list = Product.objects.filter(company=request.user.id,name__category__category=pk)
    spec = request.user.profile.specialisation
    s = Category.objects.get(id=pk)
    return render(request,'product/tovar.html', {'tovar_list':tovar_list,'spec':spec,'s':s})
class TovarCreate(CreateView):
    model = Product
    form_class = CreateTovar
    success_url=reverse_lazy('tovar_index')
    def form_valid(self, form):
        form.instance.company = self.request.user.profile

        return super().form_valid(form)
class TovarUpdate(UpdateView):
    model = Product
    form_class = CreateTovar
    success_url=reverse_lazy('tovar_index')
    def form_valid(self, form):
        form.clean()
        form.instance.company = self.request.user.profile
        return super().form_valid(form)
def delete_tovar(request, pk=None):

    tovar= get_object_or_404(Product, id=pk)
    creator= tovar.company
    if request.method == "POST" and request.user.is_authenticated and request.user.profile == creator:
        tovar.delete()
        return redirect('tovar_index')
    context= {'tovar': tovar,
              'creator': creator,
              }
    return render(request, 'product/delete_tovar.html', context)
class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderCheck
    success_url=reverse_lazy('order_index')
class OrderUpdates(UpdateView):
    model = Order
    form_class = OrderChecks
    success_url=reverse_lazy('order_index')
def index_order(request):
    tar = Tariff.objects.get(user=request.user.profile)
    spec = request.user.profile.specialisation
    order_list = Order.objects.filter(vendor=request.user).order_by('cancel','check','-date')
    request_list = Order.objects.filter(is_all=True,date__gte=request.user.date_joined).order_by('-date')
    return render(request, 'product/order.html',{'order_list':order_list,'request_list':request_list,'spec':spec,'tar':tar})
def cat_order(request, pk):
    tar = Tariff.objects.get(user=request.user.profile)
    spec = request.user.profile.specialisation
    s = Category.objects.get(id=pk)
    order_list = Order.objects.filter(vendor=request.user,item__category__category=pk).order_by('cancel', 'check', '-date')
    request_list = Order.objects.filter(is_all=True,item__category__category=pk).order_by('-date')
    return render(request, 'product/order.html', {'order_list': order_list, 'request_list': request_list,'spec':spec,'s':s,'tar':tar})
def index_review(request):
    orders = Review.objects.filter(order__vendor=request.user)
    avg = orders.aggregate(average_range=Avg('range'))
    return render(request, 'product/review.html',{'review_list':orders,'avg':avg})
def index_gallery(request):
    gallery = Gallery.objects.filter(company=request.user.id)
    return render(request, 'product/gallery.html',{'gallery':gallery})
class GalleryCreate(CreateView):
    model = Gallery
    form_class = CreateGallery
    success_url=reverse_lazy('gallery_index')
    def form_valid(self, form):
        form.instance.company = self.request.user.profile
        return super().form_valid(form)
def delete_gallery(request, pk=None):

    tovar= get_object_or_404(Gallery, id=pk)
    creator= tovar.company
    if request.method == "POST" and request.user.is_authenticated and request.user.profile == creator:
        tovar.delete()
        return redirect('gallery_index')
    context= {'tovar': tovar,
              'creator': creator,
              }
    return render(request, 'product/delete_tovar.html', context)
def index_analitic(request):
    start_date = date.today()- timedelta(days=7)
    end_date = date.today()
    queryset = Order.objects.filter(vendor=request.user)
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, 'date')
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='days')
    return render(request, 'product/analitic.html',{'values': values})
def month_analitic(request):
    start_date = date.today()+relativedelta(months=-1)
    end_date = date.today()
    queryset = Order.objects.filter(vendor=request.user)
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, 'date')
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='days')
    return render(request, 'product/analitic-m.html',{'values': values})
def _3month_analitic(request):
    start_date = date.today()+relativedelta(months=-3)
    end_date = date.today()
    queryset = Order.objects.filter(vendor=request.user)
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, 'date')
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='weeks')
    return render(request, 'product/analitic-3m.html',{'values': values})
def _6month_analitic(request):
    start_date = date.today()+relativedelta(months=-6)
    end_date = date.today()
    queryset = Order.objects.filter(vendor=request.user)
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, 'date')
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='months')
    return render(request, 'product/analitic-6m.html',{'values': values})
def year_analitic(request):
    start_date = date.today()+relativedelta(years=-1)
    end_date = date.today()
    queryset = Order.objects.filter(vendor=request.user)
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, 'date')
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='months')
    return render(request, 'product/analitic-y.html',{'values': values})
def index_tariff(request):
    tar = Tariff.objects.get(user=request.user.profile)
    return render(request, 'product/tariff.html', {'tar':tar})



