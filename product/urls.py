from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('tovar/', login_required(views.index_tovar), name='tovar_index'),
    path('tovar/new/', login_required(views.TovarCreate.as_view(template_name='product/create_tovar.html')), name='tovar_create'),
    path('tovar/<int:pk>/edit/', login_required(views.TovarUpdate.as_view(template_name='product/create_tovar.html')), name='tovar_edit'),
    path('tovar/<int:pk>/delete/', login_required(views.delete_tovar), name='tovar_delete'),
    path('order/', login_required(views.index_order),name='order_index'),
    path('order/<int:pk>/confirm/', login_required(views.OrderUpdate.as_view(template_name='product/order_edit.html')), name='order_confirm'),
    path('order/<int:pk>/cancel/', login_required(views.OrderUpdates.as_view(template_name='product/order_edit.html')), name='order_cancel'),
    path('review/', login_required(views.index_review), name='review_index'),

]
