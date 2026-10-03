from django.db import models
from datetime import timezone,datetime

# Create your models here.

class Task(models.Model):
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.completed:
            self.completed_at = datetime.now(timezone.utc)
        super().save(*args, **kwargs)

    