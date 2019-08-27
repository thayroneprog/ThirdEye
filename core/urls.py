from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
]