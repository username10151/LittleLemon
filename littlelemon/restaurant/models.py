from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Bookings(models.Model):
    name = models.CharField(max_length=255)
    numberOfGuests = models.IntegerField()
    bookingDate = models.DateField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'bookings'
        verbose_name_plural = 'Bookings'