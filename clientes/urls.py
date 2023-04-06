from django.urls import path

from clientes import views

urlpatterns = [
   path('', views.home, name='home')
]