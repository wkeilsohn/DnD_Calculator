from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('example/', views.example, name='example'),
    path('results/', views.results, name='results'), # Define Later
]