from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

def upload_path(instance,filename):
    # we can also add instance.project_name as here
    # return '/'.join(['posts',instance.project_name,filename])
    return '/'.join(['posts',filename])

# Create your models here.
class Projects(models.Model):
    temple_name = models.CharField(max_length=64) # Address
    project_name = models.CharField(primary_key=True,max_length=64) # Project Name
    decription = models.TextField()
    tel = models.CharField(max_length=64)
    email = models.EmailField()
    image = models.ImageField(default='default_project.png',upload_to='project_pic',blank=True,null=True)
    expected = models.FloatField(default=0.0)
    date = models.DateTimeField(default=timezone.now)
    pecentage = models.IntegerField(default=0)
    accepted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False) # current_balance == 
    success = models.BooleanField(default=False) # Completed project Physycally
    current_balance = models.FloatField(default=0) # This Field will update 

    def __str__(self):
        return self.project_name 


class News(models.Model):
    title = models.CharField(max_length=64)
    sub_title = models.CharField(max_length=128)
    image = models.ImageField(default='default_project.png',upload_to='news_pic',blank=True,null=True)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    username = models.CharField(max_length=64)
    projectname = models.CharField(max_length=64)
    date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(default=0)
    user_image = models.CharField(max_length=64)
    user_title = models.TextField()
    project_image = models.CharField(max_length=64)
    project_desc = models.TextField(default='')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.username


class Credit(models.Model):
    card_no = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=20)
    csv = models.CharField(max_length=5)

    def __str__(self):
        return self.username