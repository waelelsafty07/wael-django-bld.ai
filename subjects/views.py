import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers

from .models import Subjects
# Create your views here.


class Subject(View):
    def get(self,  request, *args, **kwargs):
        Subjects_all = serializers.serialize('json', Subjects.objects.all())
        return JsonResponse(json.loads(Subjects_all), safe=False)

    def post(self,  request):
        Subjects.objects.create(**json.loads(request.body))
        return JsonResponse("post", safe=False)


class SubjectID(View):

    def put(self,  request, id):
        Subjects.objects.filter(id=id).update(**json.loads(request.body))
        return JsonResponse("put", safe=False)

    def delete(self,  request, id):
        Subjects.objects.get(id=id).delete()
        return JsonResponse("delete", safe=False)
