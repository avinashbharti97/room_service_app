from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Asset(models.Model):

    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=400)


    def __str__(self):
        return self.title

class Worker(models.Model):

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length=400)


    def __str__(self):
        return self.name

class Task(models.Model):

    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=400)


    def __str__(self):
        return self.title

class AllocateTask(models.Model):

    assetId = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='asset_Task', null=True, blank=True)
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_Task', null=True, blank=True)
    workerId = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='worker_of_task', null=True, blank=True)
    timeOfAllocation = models.DateTimeField(default = timezone.now)
    taskToBePerformedBy = models.DateTimeField(default = timezone.now)
