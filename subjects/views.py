from django.shortcuts import render
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import Subjects
from .serializers import SubjectSerializer


class SubjectsView(
    generics.ListCreateAPIView
):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer


class SubjectsDetailsView(generics.DestroyAPIView,
                          generics.UpdateAPIView,
                          generics.RetrieveAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
