from rest_framework import serializers 
from api.models import CoffeePods
 
 
class ApiPodsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CoffeePods
        fields = ('id',
                  'product_type',
                  'code',
                  'coffee_flavor',
                  'pack_size'
                  )