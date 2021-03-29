from django.db import models
from Home.models import Course

# Create your models here.
class Subjects(models.Model):
    subject_id = models.CharField(max_length=20, primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dateCreate = models.DateField(auto_now_add=True)
    totalVisits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.subject_id}, {self.course_id}, {self.name}, {self.dateCreate}, {self.totalVisits}"