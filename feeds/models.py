from django.db import models
from ckeditor.fields import RichTextField


class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    profile = models.CharField(max_length=50, blank=True, null=True)
    avtar = models.FileField(upload_to='avtar', blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    cv = models.FileField(upload_to='cv', blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    mycv = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete

class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.FileField(upload_to='about_avatar', blank=True, null=True)
    about_img = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    tech = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skill


class Achievements(models.Model):
    achievement = models.CharField(max_length=250, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    certificate_id = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.achievement


class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



