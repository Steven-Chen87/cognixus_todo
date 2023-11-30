from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=255)  # Renamed from "task" to "taskName"
    taskDescription = models.TextField(blank=True, null=True)  # New "taskDescription" field
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.taskName