import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from .forms import StudentForm

from .models import Students
# Create your views here.


class Student(View):
    def get(self,  request, *args, **kwargs):
        Students_all = serializers.serialize('json', Students.objects.all())
        return JsonResponse(json.loads(Students_all), safe=False)

    def post(self,  request):
        try:
            form = StudentForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.errors, status=422)
        except:
            return JsonResponse({'message': 'Unknown Format'}, status=500)


class StudentID(View):

    def put(self,  request, id):
        Students.objects.filter(id=id).update(**json.loads(request.body))
        return JsonResponse("put", safe=False)

    def delete(self,  request, id):
        Students.objects.get(id=id).delete()
        return JsonResponse("delete", safe=False)
