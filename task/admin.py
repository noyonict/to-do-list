from django.contrib import admin
from .models import Task


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_completed', 'is_deleted', 'serial_number', 'create_at']
    list_display_links = ['name', 'create_at']
    list_editable = ['is_completed', 'is_deleted', 'serial_number']
    list_filter = ['create_at', 'update_at']
    search_fields = ['name', ]

    class Meta:
        model = Task


admin.site.register(Task, TaskModelAdmin)
