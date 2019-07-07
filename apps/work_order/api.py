from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import Worker, WorkOrder
from .serializers import WorkerSerializer, WorkOrderSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class WorkOrderViewSet(viewsets.ModelViewSet):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = ('deadline',)

    @action(detail=True, url_name='assign', url_path='assign/(?P<worker_id>[0-9]+)')
    def assign(self, request, pk=None, worker_id=None):
        try:
            work_order = self.get_object()
            worker_count = work_order.workers.all().count()
            if worker_count >= 5:
                raise APIException({"errors": ["Maximum worker allocated."]})
            worker = Worker.objects.get(pk=worker_id)
            work_order.workers.add(worker)
        except Worker.DoesNotExist:
            raise APIException({"errors": ["Requested worker does not exists."]})
        return Response({"message": "{} assigned to {}".format(worker.name, work_order.title)})

    @action(detail=True, url_name='unassigned', url_path='unassigned/(?P<worker_id>[0-9]+)')
    def unassigned(self, request, pk=None, worker_id=None):
        work_order = self.get_object()
        try:
            worker = Worker.objects.get(pk=worker_id)
            work_order.workers.remove(worker_id)
        except Worker.DoesNotExist:
            raise APIException({"errors": ["Requested worker does not exists."]})
        return Response({"message": "{} unassigned from {}".format(worker.name, work_order.title)})
