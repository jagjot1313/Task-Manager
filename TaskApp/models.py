from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    dateCreated=models.DateField()
    deadlineDate=models.DateField()
    completionStatus=models.BooleanField(default=False)
    class Meta:
        db_table='task'