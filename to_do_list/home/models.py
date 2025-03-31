from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_descr = models.TextField()

    def __str__(self):
        return self.task_name
    

class Completed_task(models.Model):
    task_name = models.CharField(max_length=30)
    task_descr = models.TextField()

    def __str__(self):
        return f"Completed task {self.task_name}"