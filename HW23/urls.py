from django.urls import path
from . import views


urlpatterns = [
    path('custom-page/', views.custom_page, name='custom-page'),
    path('', views.home, name='home'), 
]