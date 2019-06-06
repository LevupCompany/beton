from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('company/<int:pk>/', views.company, name='company'),
    path('<city_slug>/', views.city, name='catalog_city'),
    path('<city_slug>/<cat_slug>/', views.category, name='catalog_category'),
    path('<city_slug>/<cat_slug>/<subcat_slug>/', views.subcategory, name='catalog_subcategory'),
    path('<city_slug>/<cat_slug>/<subcat_slug>/<tovar_slug>/', views.tovar, name='catalog_tovar'),
    path('search',views.search,name='catalog_search'),
]
