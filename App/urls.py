from .views import *
from django.urls import path

urlpatterns= [
    path('home1/',home1,name='home1'),
   path('product/',product,name='product'),
   path('about/',about,name='about'),
   path('login/',login,name='login')


]