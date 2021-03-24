from django.db import models

# Model Member
class Member(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    userName = models.CharField(null=True, max_length=50)
    sex = models.BooleanField(null=True)
    point = models.IntegerField(default=0)
    dateCreate = models.DateTimeField()
    status = models.BooleanField()
    activeCount = models.IntegerField(null=True)



