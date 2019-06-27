from django.urls import path
from .views import TaskView


app_name = 'task'

urlpatterns = [
    path('v1/api/', TaskView.as_view(), name='task-list'),
    path('v1/api/<task_id>/', TaskView.as_view(), name='single-task'),
]
