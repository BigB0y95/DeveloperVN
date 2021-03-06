# Generated by Django 3.1.4 on 2021-04-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_course_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='image/banner')),
                ('createDate', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('logo_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='image/logo')),
                ('createDate', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
