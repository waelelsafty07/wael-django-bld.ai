from django.shortcuts import render
from parents.middleware import Authenticate
from parents.permision import ParentDetailPermissions, ParentPermissions
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parents
from .serializers import ParentSerializer


class ParentsView(APIView):
    authentication_classes = [Authenticate]
    permission_classes = [ParentPermissions]

    def get(self, request):
        data = ParentSerializer(Parents.objects.all(), many=True)
        return Response(data.data)

    def post(self, request):

        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ParentsDetailsView(APIView):
    authentication_classes = [Authenticate]
    permission_classes = [ParentDetailPermissions]

    def put(self, request, id):
        serializer = ParentSerializer(
            data=request.data, instance=Parents.objects.get(id=id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, id):
        try:
            serializer = ParentSerializer(Parents.objects.get(id=id))
            return Response(serializer.data)
        except Parents.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            Parents.objects.get(id=id).delete()
            return Response(status=status.HTTP_200_OK)
        except Parents.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
