from rest_framework import serializers
from .models import Parents


class ParentSerializer(serializers.ModelSerializer):
    # comment this line when using mixins
    # to use products inside category, many: to deal with lists
    # parent = ProductListSerializer(many=True)

    class Meta:
        model = Parents
        fields ="__all__"
