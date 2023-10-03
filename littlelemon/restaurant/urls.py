from django.urls import path
from . import views
from .views import menuView, bookingView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuView.as_view(), name='menu'),
    path('booking/', bookingView.as_view(), name='booking'),
]