from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=["title","description","completed"]

        read_only_fields=['id','created_at','completed_at']
    
