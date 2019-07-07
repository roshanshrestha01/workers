from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return '{} from {}'.format(self.name, self.company_name)


class WorkOrder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    worker = models.ManyToManyField(Worker, related_name='work_orders')

    def __str__(self):
        return self.title
