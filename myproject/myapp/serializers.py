from .models import student
from  rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'