from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        # fields = '__all__'
        read_only_fields = ('is_completed', 'is_deleted', 'create_at', 'update_at')
        exclude = ('delete_at',)
