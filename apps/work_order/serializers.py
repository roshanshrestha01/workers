from rest_framework import serializers

from .models import Worker, WorkOrder


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'
        depth = 1


class SpecificWorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ('title', 'description', 'deadline')


class WorkerDetailSerializer(serializers.ModelSerializer):
    work_orders = SpecificWorkOrderSerializer(many=True)

    class Meta:
        model = Worker
        fields = '__all__'
