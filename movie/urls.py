from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies-chart/', views.movies_by_year_chart, name='movies_chart'),
]