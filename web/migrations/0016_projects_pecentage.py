# Generated by Django 3.0.5 on 2020-08-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_news_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='pecentage',
            field=models.IntegerField(default=0),
        ),
    ]
