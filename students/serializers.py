from rest_framework import serializers
from subjects.serializers import SubjectSerializer
from .models import Students
from parents.serializers import ParentSerializer


def check_mark(value):
    if value < 0:
        raise serializers.ValidationError("mark must be greater than 0")


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


class StudentSerializer(serializers.ModelSerializer):

    mark = serializers.IntegerField(validators=[check_mark])

    parent = ParentSerializer()
    subjects = SubjectSerializer()

    class Meta:
        model = Students
        fields = '__all__'

    # def get_fields(self, *args, **kwargs):
    #     fields = super(StudentSerializer, self).get_fields(*args, **kwargs)
    #     request = self.context.get('request', None)
        # 	if request.method == "POST":
        # 		fields['mark'].required = False

        # 	return fields
