# Generated by Django 3.1.7 on 2021-04-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sponsor', '0004_auto_20210401_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
