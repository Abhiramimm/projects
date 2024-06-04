from rest_framework import serializers

from api.models import Employee,Task

class TaskSerializer(serializers.ModelSerializer):

    employee_obj=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Task

        fields="__all__"

        read_only_fields=["id","employee_obj"]


class EmployeeSerializer(serializers.ModelSerializer):

    tasks=TaskSerializer(many=True,read_only=True)

    class Meta:

        model=Employee

        fields=["id","name","department","salary","tasks"]


