# Generated by Django 4.0.4 on 2022-09-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_courses_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.CharField(default='This is a test description', max_length=255),
        ),
    ]
