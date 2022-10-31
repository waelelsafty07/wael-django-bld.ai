from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import Students
from .serializers import StudentSerializer


class StudentsView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   ):
    queryset = Students.objects.all().prefetch_related("subjects")
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentsDetailsView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
