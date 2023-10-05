from rest_framework import serializers
from .models import Menu, Bookings

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'