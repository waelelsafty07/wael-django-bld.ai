
import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers

from .models import Parents
# Create your views here.


class Parent(View):
    def get(self,  request, *args, **kwargs):
        Parents_all = serializers.serialize('json', Parents.objects.all())
        return JsonResponse(json.loads(Parents_all), safe=False)

    def post(self,  request):
        Parents.objects.create(**json.loads(request.body))
        return JsonResponse("post", safe=False)


class ParentID(View):

    def put(self,  request, id):
        Parents.objects.filter(id=id).update(**json.loads(request.body))
        return JsonResponse("put", safe=False)

    def delete(self,  request, id):
        Parents.objects.get(id=id).delete()
        return JsonResponse("delete", safe=False)
