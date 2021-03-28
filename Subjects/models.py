from django.db import models
from django.core.files.storage import FileSystemStorage

subject_image_folder = FileSystemStorage(location= '/static/image/course')
# Model Subjects
class Subjects(models.Model):
    subject_id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to = 'image/course')
    dateCreate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject_id}, {self.name}, {self.content}, {self.image}, {self.dateCreate}"

class Subjects_Children(models.Model):
    sub_chil_id = models.CharField(max_length=10, primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    totalVisits = models.IntegerField(default=0)

    def __str__(self):
        return  f"{self.sub_chil_id}, {self.subject_id}, {self.totalVisits}"
