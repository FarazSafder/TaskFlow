from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializers
from .models import Task


# Create your views here.

class TaskView(ModelViewSet):
    serializer_class = TaskSerializers
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        ).order_by("-created_at")
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)