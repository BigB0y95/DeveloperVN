# Generated by Django 3.1.4 on 2021-04-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sponsor', '0003_sponsor_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='money',
            field=models.CharField(max_length=12),
        ),
    ]