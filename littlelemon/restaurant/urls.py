from django.urls import path
from . import views
from .views import menuView, bookingView, SingleMenuItemView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='singleMenuItem'),
    path('booking/', bookingView.as_view(), name='booking'),
]