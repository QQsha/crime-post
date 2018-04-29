from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('news/<slug:slug1>/<slug:slug2>/', views.main_page, name='main_page'),
]