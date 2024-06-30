from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import MongoModel
import json

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mongo_crud(request):
    if request.method == 'GET':
        data = list(MongoModel.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')

            if not name:
                return JsonResponse({'error': 'Field "name" is required'}, status=400)

            obj = MongoModel.objects.create(name=name)
            return JsonResponse({'id': str(obj.id), 'name': obj.name}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def mongo_detail(request, pk):
    try:
        obj = MongoModel.objects.get(pk=pk)
    except MongoModel.DoesNotExist:
        return JsonResponse({'error': f'Object with id {pk} not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({'id': str(obj.id), 'name': obj.name})

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            name = data.get('name')

            if not name:
                return JsonResponse({'error': 'Field "name" is required'}, status=400)

            obj.name = name
            obj.save()
            return JsonResponse({'id': str(obj.id), 'name': obj.name})

        except json.JSONDecodeError:
            print('here')
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)

    elif request.method == 'DELETE':
        try:
            obj.delete()
            return JsonResponse({'message': 'Object deleted successfully!'})

        except MongoModel.DoesNotExist:
            print('here')
            return JsonResponse({'error': f'Object with id {pk} not found'}, status=404)

    else:
        # Handle other HTTP methods
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
