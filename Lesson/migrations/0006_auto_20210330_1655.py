# Generated by Django 3.1.4 on 2021-03-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0005_lesson_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='url_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
