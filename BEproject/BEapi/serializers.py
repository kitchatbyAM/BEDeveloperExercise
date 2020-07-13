from rest_framework import serializers
from .models import Task
from django.db import models
from django.contrib.auth.models import User

class TaskListSerializer(serializers.HyperlinkedModelSerializer):
    userid = serializers.ReadOnlyField(source='userid.username')

    class Meta:
        model = Task
        fields = ['url', 'taskid', 'userid', 'tasktitle',
                  'taskdescription', 'taskstate', 'taskduedate']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']


