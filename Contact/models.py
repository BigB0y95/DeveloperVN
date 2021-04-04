from django.db import models

# Create your models here.
class Contact_User(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_person = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=13)
    content  = models.TextField()
    createDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.contact_id}, {self.contact_person}, {self.mail}, {self.phone}, {self.content}, {self.createDate}, {self.status}"

class Contact_Live(models.Model):
    contact_live_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    url = models.CharField(max_length=255, null =True, blank = True)
    icon = models.CharField(max_length=255)
    createDate =  models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.contact_live_id}, {self.name}, {self.content}, {self.url}, {self.icon}, {self.createDate}, {self.status}"