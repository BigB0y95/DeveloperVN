from django.db import models
from Subjects.models import Subjects

# Create your models here.
class Lesson(models.Model):
    lesson_id = models.CharField(max_length=25, primary_key=True)
    subject_id = models.ForeignKey(Subjects,default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'image/lesson')
    time = models.CharField(max_length=20, null=True)
    views = models.IntegerField(default=0)
    dateCreate = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=255, null=True)
    url_name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return f"{self.lesson_id}, {self.subject_id}, {self.name}, {self.content}, {self.url}, {self.image}, {self.time}, {self.views}, {self.dateCreate}, {self.author}, {self.url_name}"

