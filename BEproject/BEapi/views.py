from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskListSerializer, UserSerializer
from .models import Task

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('taskduedate')
#     serializer_class = TaskListSerializer

class TaskList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })
