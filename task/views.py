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
        all_task = [t.name for t in Task.objects.filter(is_deleted=False)]
        return Response(all_task)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        task = get_object_or_404(Task, id=id)
        if task:
            task.is_completed = not task.is_completed
            task.save()
        return Response({'is_completed': task.is_completed})

    def delete(self, request, id, format=None):
        task = get_object_or_404(Task, id=id)
        if task:
            task.is_deleted = True
            task.delete_at = datetime.now()
            task.save()
        return Response({'details': str(task.name) + ' Deleted!'})
