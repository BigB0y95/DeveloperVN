from django.db import models

# Create your models here.
class Info_Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'image/sponsor', null = True)
    account = models.CharField(max_length=30)
    recipients = models.CharField(max_length=100)
    dateCreate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_id}, {self.name}, {self.image}, {self.account}, {self.recipients}, {self.dateCreate}, {self.status}"

class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Info_Account, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    money = models.CharField(max_length=12)
    message = models.CharField(max_length=500)
    sentDate = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sponsor_id}, {self.sender}, {self.money}, {self.message}, {self.sentDate}, {self.status}"
