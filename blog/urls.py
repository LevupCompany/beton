from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('<slug>', views.view, name='news_view'),

]
