from django.shortcuts import render
#Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
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

class bookingView(APIView):
    def get(self, request):
        items = Bookings.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})