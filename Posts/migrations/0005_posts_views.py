# Generated by Django 3.1.4 on 2021-04-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_auto_20210406_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
