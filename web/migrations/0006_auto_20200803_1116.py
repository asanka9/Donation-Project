# Generated by Django 3.0.5 on 2020-08-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200803_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='default_project.png', upload_to='project_pic'),
        ),
    ]
