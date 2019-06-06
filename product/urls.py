from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('tovar/', views.index_tovar, name='tovar_index'),
    path('tovar/<int:pk>', views.cat_tovar, name='tovar_cat'),
    path('tovar/new/', views.TovarCreate.as_view(template_name='product/create_tovar.html'), name='tovar_create'),
    path('tovar/<int:pk>/edit/', views.TovarUpdate.as_view(template_name='product/create_tovar.html'), name='tovar_edit'),
    path('tovar/<int:pk>/delete/', views.delete_tovar, name='tovar_delete'),
    path('order/', views.index_order,name='order_index'),
    path('order/<int:pk>/', views.cat_order, name='order_cat'),
    path('order/<int:pk>/confirm/', views.OrderUpdate.as_view(template_name='product/order_edit.html'), name='order_confirm'),
    path('order/<int:pk>/cancel/', views.OrderUpdates.as_view(template_name='product/order_edit.html'), name='order_cancel'),
    path('review/', views.index_review, name='review_index'),
    path('gallery/', views.index_gallery, name='gallery_index'),
    path('gallery/new/', views.GalleryCreate.as_view(template_name='product/create_tovar.html'),
         name='gallery_create'),
    path('gallery/<int:pk>/delete/', views.delete_gallery, name='gallery_delete'),
    path('analitic/', views.index_analitic, name='analitic_index'),
    path('analitic/m/', views.month_analitic, name='analitic_m'),
    path('analitic/3m/', views._3month_analitic, name='analitic_3m'),
    path('analitic/6m/', views._6month_analitic, name='analitic_6m'),
    path('analitic/y/', views.year_analitic, name='analitic_y'),
    path('plan/', views.index_tariff, name='tariff_index'),

]
