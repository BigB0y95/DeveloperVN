from django.db import models
from django.core.files.storage import FileSystemStorage

subject_image_folder = FileSystemStorage(location= '/media/image/course')
# Model Subjects
class Subjects(models.Model):
    subject_id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=200, null=True)
    image = models.ImageField(storage = subject_image_folder)
    dateCreate = models.DateField(auto_now_add=True)

class Subjects_Children(models.Model):
    sub_chil_id = models.CharField(max_length=10, primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    totalVisits = models.IntegerField(default=0)
