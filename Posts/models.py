from django.db import models

# Create your models here.
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    describe = models.CharField(max_length=1000)
    image = models.ImageField(upload_to= 'image/posts', null=True)
    url = models.TextField(null=True, blank=True)
    content = models.TextField()
    createDate = models.DateField(auto_now_add=True)
    url_name = models.CharField(max_length=350)
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.post_id}, {self.name}, {self.describe}, {self.image}, {self.url}, {self.content}, {self.createDate}, {self.url_name}, {self.views}, {self.status}"