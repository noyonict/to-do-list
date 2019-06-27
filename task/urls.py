from django.urls import path
from .views import TaskView


app_name = 'task'

urlpatterns = [
    path('v1/api/', TaskView.as_view(), name='task-list')
]
