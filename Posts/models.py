from django.db import models

# Create your models here.
class Posts(models.Model):
    Post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    describe = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField()
    createDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Post_id}, {self.name}, {self.describe}, {self.url}, {self.content}, {self.createDate}, {self.status}"