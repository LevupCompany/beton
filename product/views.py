from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Avg
from django.contrib.auth.models import User
from catalog.models import Order, Count, Order, Review
def index_tovar(request):
    tovar_list = Product.objects.filter(company=request.user.id)

    return render(request,'product/tovar.html', {'tovar_list':tovar_list})
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
    order_list = Order.objects.filter(vendor=request.user).order_by('cancel','check','-date')
    request_list = Order.objects.filter(is_all=True).order_by('-date')
    return render(request, 'product/order.html',{'order_list':order_list,'request_list':request_list})
def index_review(request):
    orders = Review.objects.filter(order__vendor=request.user)
    avg = orders.aggregate(average_range=Avg('range'))
    return render(request, 'product/review.html',{'review_list':orders,'avg':avg})
