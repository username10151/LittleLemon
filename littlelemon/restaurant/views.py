from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

class SingleMenuItemView(APIView):
    def get(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
            serializer = menuSerializer(menu_item)
            return Response(serializer.data)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
            serializer = menuSerializer(menu_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
            menu_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)