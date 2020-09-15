from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import CoffeeMachines , CoffeePods
from api.serializers import ApiSerializer
from api.serializerspod import ApiPodsSerializer


#CoffeeMachines
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
#Add CoffeeMachines
@csrf_exempt
def add_coffeemachine(request):
    if request.method == 'POST':
        api_data = JSONParser().parse(request)
        api_serializer = ApiSerializer(data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()    
            return JsonResponse(api_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Show all CoffeeMachines
def show_coffeemachine(request):
    if request.method == 'GET':
        api = CoffeeMachines.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            api = api.filter(title__icontains=title)
        
        api_serializer = ApiSerializer(api, many=True)
        return JsonResponse(api_serializer.data, safe=False)
        
#Show CoffeeMachines by code
def api_coffeemachine_detail(request,id):
    
    try:
        post = CoffeeMachines.objects.get(code=id)
    except CoffeeMachines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ApiSerializer(post)
        return JsonResponse(serializer.data)

@api_view(['DELETE'])
#Delete CoffeeMachines by code
@csrf_exempt
def api_coffeemachine_delete(request,id):

    try:
        post = CoffeeMachines.objects.get(code=id)
    except CoffeeMachines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()             
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)             



#CoffeePods
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
#Add CoffeePods
@csrf_exempt
def add_coffeepod(request):
    if request.method == 'POST':
        api_data = JSONParser().parse(request)
        api_serializer = ApiPodsSerializer(data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()
            return JsonResponse(api_serializer.data, status=status.HTTP_201_CREATED) 
    else:
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Show all CoffeeMachines
def show_coffeepod(request):
    if request.method == 'GET':
        api = CoffeePods.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            api = api.filter(title__icontains=title)
        
        api_serializer = ApiPodsSerializer(api, many=True)
        return JsonResponse(api_serializer.data, safe=False)
        
#Show CoffeeMachines by code
def api_coffeepod_detail(request,id):
    
    try:
        post = CoffeePods.objects.get(code=id)
    except CoffeePods.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ApiPodsSerializer(post)
        return JsonResponse(serializer.data)

@api_view(['DELETE'])
#Delete CoffeeMachines by code
@csrf_exempt
def api_coffeepod_delete(request,id):

    try:
        post = CoffeePods.objects.get(code=id)
    except CoffeePods.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()             
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)                     