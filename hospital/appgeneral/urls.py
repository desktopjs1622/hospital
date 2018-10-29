from django.urls import path
from appgeneral.views import index

name = 'appgeneral'
urlpatterns = [
    path('inicio', index, name='index')

]