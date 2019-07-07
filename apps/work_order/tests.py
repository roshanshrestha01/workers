from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Worker, WorkOrder


class WorkerTests(APITestCase):

    def test_create_worker(self):
        """
        Ensure we can create a new worker object.
        """
        url = reverse('api:worker-list')
        data = {'name': 'Roshan Shrestha', 'company_name': 'ZXY Company', 'email': 'roshan@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Worker.objects.get().name, 'Roshan Shrestha')
        self.assertEqual(Worker.objects.count(), 1)

    def test_delete_worker(self):
        """
        Ensure we can delete a new worker object.
        """
        worker = Worker.objects.create(name="Roshan Shrestha", company_name='XYA Company', email="roshan@gmail.com")

        url = reverse('api:worker-detail', kwargs={"pk": worker.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class WorkOrderTests(APITestCase):

    def test_create_work_order(self):
        """
        Ensure we can create a new worker object.
        """
        url = reverse('api:workorder-list')
        data = {
            'title': 'Setup client url',
            'description': 'Creating client working endpoint',
            'deadline': '2019-05-27'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorkOrder.objects.get().title, 'Setup client url')
        self.assertEqual(WorkOrder.objects.count(), 1)

    def test_assign_work_order(self):
        """
        Ensure we can create a new worker object.
        """
        worker = Worker.objects.create(
            name="Roshan Shrestha",
            company_name='XYA Company',
            email="roshan@gmail.com"
        )
        work_order = WorkOrder.objects.create(
            title="Setup client url",
            description="Creating client endpoint",
            deadline="2019-05-27"
        )
        url = reverse("api:workorder-assign", kwargs={"pk": work_order.id, "worker_id": worker.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(work_order.workers.all().count(), 1)
