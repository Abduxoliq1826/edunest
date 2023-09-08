from django.db import models
from django.contrib.auth.models import AbstractUser

# Home
class User(AbstractUser):
    status = models.IntegerField(choices=((1, 'user'), (2, 'admins')), default=1)
    number = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to="user", null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)



class Course(models.Model):
    image = models.ImageField(upload_to='Course')
    name = models.CharField(max_length=255)
    text = models.TextField()
    teacher_name = models.CharField(max_length=255)
    teacher_ielts = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.CharField(max_length=255)
    schedule_start = models.CharField(max_length=255)
    schedule_finish = models.CharField(max_length=255)

class Mock(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    date = models.DateTimeField()
    status = models.IntegerField(choices=((1, "Active"), (2, "Disactive")), default=1)


class Student(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    cource = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=True)
    mock = models.ForeignKey(Mock, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.IntegerField(choices=((1, "New"), (2, "Deleted"), (3, "Finished")), default=1)


class Link(models.Model):
    link = models.URLField()
    name = models.IntegerField(choices=((1, "Telegram"), (2, "Instagram"), (3, "Facebook"), (4, "Twitter")), default=1)

