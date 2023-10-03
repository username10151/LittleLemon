from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu, Bookings
from .serializers import menuSerializer, bookingsSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class bookingView(APIView):
    def get(self, request):
        items = Bookings.objects.all()
        serializer = bookingsSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = bookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})
        
class menuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})