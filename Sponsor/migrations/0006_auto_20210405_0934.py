# Generated by Django 3.1.4 on 2021-04-05 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sponsor', '0005_auto_20210403_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='account_id',
            new_name='account',
        ),
    ]