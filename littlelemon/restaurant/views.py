from django.shortcuts import render
#Rest Framework
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
#Local
from .models import Menu, Bookings
from .serializers import menuSerializer, bookingSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class bookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bookings.objects.all()
    serializer_class = bookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]
