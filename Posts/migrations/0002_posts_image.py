# Generated by Django 3.1.4 on 2021-04-06 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(null=True, upload_to='image/posts'),
        ),
    ]