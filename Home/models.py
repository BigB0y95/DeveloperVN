from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    about = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to = 'image/course')
    dateCreate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course_id}, {self.name}, {self.about}, {self.content}, {self.image}, {self.dateCreate}, {self.status}"

class Logo(models.Model):
    logo_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'image/logo')
    createDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.logo_id}, {self.image}, {self.createDate}, {self.status}"

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'image/banner')
    createDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.banner_id}, {self.image}, {self.createDate}, {self.status}"
