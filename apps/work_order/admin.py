from django.contrib import admin

from .models import Worker, WorkOrder


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'email', ]
    search_fields = ['name', 'company_name', 'email', ]


admin.site.register(Worker, WorkerAdmin)


class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', ]
    search_fields = ['title', ]


admin.site.register(WorkOrder, WorkOrderAdmin)
