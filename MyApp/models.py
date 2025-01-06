from django.db import models

class Person(models.Model):
    dni = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Makers(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.FloatField()
    maker = models.ForeignKey(Makers, on_delete=models.CASCADE)
    
    # Changes
    image = models.URLField(null=True, default='https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg')
    price = models.FloatField()    
    unit = models.CharField(max_length=5)


    def __str__(self):
        return self.name + " - " + self.maker.name

class Event(models.Model):
    events_types = (
        ('P', 'Purchase'),
        ('S', 'Sale'),
        ('PL', 'Products Loss'),
        ('PE', 'Products Entry'),
    )
    type = models.CharField(max_length=2, choices=events_types)
    part = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField()
    amount = models.FloatField()
    
class EventDetail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    varProduct = models.FloatField()
    money = models.FloatField()
    
