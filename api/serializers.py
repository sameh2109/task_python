from rest_framework import serializers 
from api.models import CoffeeMachines
 
 
class ApiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CoffeeMachines
        fields = ('id',
                  'product_type',
                  'code',
                  'water_line_compatible',
                  'model'
                  )
