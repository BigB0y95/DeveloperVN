from django.db import models

# Model Member
class Member(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    userName = models.CharField(null=True, max_length=50)
    sex = models.BooleanField(null=True)
    point = models.IntegerField(default=0)
    dateCreate = models.DateField(auto_now_add=True)
    status = models.BooleanField()
    activeCount = models.IntegerField(null=True)

    class Meta:
        ordering = ("id", "email", "password", "birthday", "userName", "sex", "point", "dateCreate", "status", "activeCount")
    def __str__(self):
        return f"{self.email}, {self.password}, {self.birthday}, {self.userName}, {self.sex}, {self.point}, {self.dateCreate}, {self.status}, {self.activeCount}"



