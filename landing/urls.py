from django.urls import path
from django.conf.urls import include
from landing import views
from django.conf.urls import url

urlpatterns = [
    
    path('',views.index, name='index'),
]
