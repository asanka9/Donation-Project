# Generated by Django 3.0.5 on 2020-08-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200803_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='project_pic'),
        ),
    ]
