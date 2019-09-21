from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
    path('index/', views.index_view, name='index_view'),
]