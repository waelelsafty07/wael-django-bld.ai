from unicodedata import name
from rest_framework import serializers
from students.models import Students
from .models import Subjects
from parents.serializers import ParentSerializer


# class ProductListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Students
#         fields = ['name']

# To show category data when getting product


# class CategorySerializer(serializers.ModelSerializer):
#     # comment this line when using mixins
#     # to use products inside category, many: to deal with lists
#     products = ProductListSerializer(many=True)

#     class Meta:
#         model = Category
#         fields = ['name']

# class StudentsListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Subjects
#         fields = ["firstname", "lastname"]


class SubjectSerializer(serializers.ModelSerializer):
    # students = StudentsListSerializer(many=True)
    # name = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subjects
        fields = '__all__'
