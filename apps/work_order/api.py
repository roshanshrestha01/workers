from rest_framework import viewsets

from .models import Worker, WorkOrder
from .serializers import WorkerSerializer, WorkOrderSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class WorkOrderViewSet(viewsets.ModelViewSet):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
