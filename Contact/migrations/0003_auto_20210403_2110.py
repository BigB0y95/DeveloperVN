# Generated by Django 3.1.7 on 2021-04-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_auto_20210403_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_live',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
