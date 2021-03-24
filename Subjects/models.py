from django.db import models

# Model Subjects
class Subjects(models.Model):
    subject_id = models.CharField(max_length=2, primary_key=True)
    name = models.TextField(max_length=200)
