from django.db import models
from django.utils import timezone


# Create your models here.


class Task(models.Model):
    class TaskStates(models.TextChoices):
        TODO = 'To do'
        INPROGRESS = 'In progress'
        DONE = 'Done'

    taskid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE, default = None)
    tasktitle = models.CharField(max_length=100, blank=True, default='')
    taskdescription = models.TextField(blank=True)
    taskstate = models.CharField(max_length=50, choices=TaskStates.choices,  default=TaskStates.TODO)
    taskduedate = models.DateField(blank=True, default = None)

    def __str__(self):
        return self.tasktitle

