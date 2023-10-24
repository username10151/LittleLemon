from django.urls import path
from . import views
from .views import menuView, bookingView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='singleMenuItem'),
    path('booking/', bookingView.as_view(), name='booking'),
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]