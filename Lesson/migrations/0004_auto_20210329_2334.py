# Generated by Django 3.1.7 on 2021-03-29 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0002_auto_20210329_1430'),
        ('Lesson', '0003_auto_20210329_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subject_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Subjects.subjects'),
        ),
    ]
