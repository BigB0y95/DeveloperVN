# Generated by Django 3.1.4 on 2021-04-01 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0006_auto_20210330_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]