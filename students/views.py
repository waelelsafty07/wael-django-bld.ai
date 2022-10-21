import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers

from .models import Students
# Create your views here.


class Student(View):
    def get(self,  request, *args, **kwargs):
        Students_all = serializers.serialize('json', Students.objects.all())
        return JsonResponse(json.loads  (Students_all), safe=False)

    def post(self,  request):
        Students.objects.create(**json.loads(request.body))
        return JsonResponse("post", safe=False)

    def put(self,  request, id):
        Students.objects.filter(id=id).update(**json.loads(request.body))
        return JsonResponse("put", safe=False)

    def delete(self,  request, id):
        Students.objects.get(id=id).delete()
        return JsonResponse("delete", safe=False)
