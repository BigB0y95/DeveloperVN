# Generated by Django 3.1.4 on 2021-03-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
