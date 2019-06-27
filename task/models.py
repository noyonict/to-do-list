from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=250, help_text='Name of the task')
    is_completed = models.BooleanField(default=False, help_text='The task is completed or not.')
    is_deleted = models.BooleanField(default=False, help_text='The task is deleted for the user or not.')
    serial_number = models.PositiveIntegerField(default=1, help_text='How the task is order')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True, blank=True, help_text='When the task is deleted by the user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['serial_number', '-create_at']
        db_table = 'task'
        app_label = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


