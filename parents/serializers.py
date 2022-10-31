from rest_framework import serializers
from students.models import Students
from .models import Parents


class StudentSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    childern = StudentSerializerList(
        many=True)

    class Meta:
        model = Parents
        fields = "__all__"
