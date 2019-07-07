from . import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('workers', api.WorkerViewSet)
router.register('work-orders', api.WorkOrderViewSet)
