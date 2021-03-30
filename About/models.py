from django.db import models

# Create your models here.
class About(models.Model):
    about_id = models.AutoField(primary_key=True)
    content = models.TextField()
    createDate = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.about_id}, {self.content}, {self.createDate}, {self.author}, {self.status}"
