from django.db import models

# Create your models here.

class CoffeeMachines(models.Model):
    product_type = models.CharField(max_length=70, blank=False, choices=[('COFFEE_MACHINE_LARGE','COFFEE_MACHINE_LARGE'),('COFFEE_MACHINE_SMALL','COFFEE_MACHINE_SMALL'),('ESPRESSO_MACHINE','ESPRESSO_MACHINE')])
    code = models.CharField(max_length=200,blank=False, default='', unique= True  )
    water_line_compatible = models.BooleanField(default=False)
    model = models.CharField(max_length=200,blank=False, choices=[('base','base'),('premium','premium'),('delux','delux')])

class CoffeePods(models.Model):    
    product_type = models.CharField(max_length=70, blank=False, choices=[('COFFEE_POD_LARGE','COFFEE_POD_LARGE'),('COFFEE_POD_SMALL','COFFEE_POD_SMALL'),('ESPRESSO_POD','ESPRESSO_POD')])
    code = models.CharField(max_length=200,blank=False, default='', unique= True)
    coffee_flavor = models.CharField(max_length=70, blank=False, choices=[('COFFEE_FLAVOR_VANILLA','COFFEE_FLAVOR_VANILLA'),('COFFEE_FLAVOR_CARAMEL','COFFEE_FLAVOR_CARAMEL'),('COFFEE_FLAVOR_PSL','COFFEE_FLAVOR_PSL'),('COFFEE_FLAVOR_MOCHA','COFFEE_FLAVOR_MOCHA'),('COFFEE_FLAVOR_HAZELNUT','COFFEE_FLAVOR_HAZELNUT')])
    pack_size = models.CharField(max_length=70, blank=False, choices=[('1 dozen','1 dozen'),('3 dozen','3 dozen'),('5 dozen','5 dozen'),('7 dozen','7 dozen')])    