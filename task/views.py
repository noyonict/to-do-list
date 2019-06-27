from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404
from .models import Task
from .serializer import TaskSerializer
from datetime import datetime


class TaskView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)
    def get(self, request):
        all_task = Task.objects.filter(is_deleted=False)
        serializer = TaskSerializer(all_task, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, task_id, format=None):
        task = get_object_or_404(Task, id=task_id)
        if task:
            task.is_completed = not task.is_completed
            task.save()
            return Response({'name': task.name, 'is_completed': task.is_completed})
        return Response({'details': 'Task is not found!'})

    def delete(self, request, task_id, format=None):
        task = get_object_or_404(Task, id=task_id)
        if task:
            task.is_deleted = True
            task.delete_at = datetime.now()
            task.save()
            return Response({'details': str(task.name) + ' Deleted!'})
        return Response({'details': 'Task is not found!'})
