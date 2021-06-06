from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASECADE, default=None)
    Student_Name = models.CharField(max_length=100)
    Attendance = models.BooleanField(default=False)
    Score = models.IntegerField(default=0)

    def __str__(self):
        return self.Student_Name + " - " + str(self.Attendance) 