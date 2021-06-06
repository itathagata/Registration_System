from django.db import models

# Create your models here.
class TaskList(models.Model):
    Student_Name = models.CharField(max_length=100)
    Attendance = models.BooleanField(default=False)
    Score = models.IntegerField(default=0)

    def __str__(self):
        return self.Student_Name + " - " + str(self.Attendance) 