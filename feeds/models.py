from django.db import models


class PersonalInformation(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    profile = models.CharField(max_length=50, blank=True, null=True)
    profile_avatar = models.FileField(upload_to="profile_avatar", blank=True, null=True)
    avatar_link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    resume = models.FileField(upload_to="resume", blank=True, null=True)
    resume_link = models.URLField(blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            existing = PersonalInformation.objects.get(pk=self.pk)
            if existing.resume and existing.resume != self.resume:
                existing.resume.delete(save=False)  # Delete old resume

            if (
                existing.profile_avatar
                and existing.profile_avatar != self.profile_avatar
            ):
                existing.profile_avatar.delete(save=False)

        # Proceed with saving new file
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete resume when instance is deleted
        if self.resume:
            self.resume.delete(save=False)

        if self.profile_avatar:
            self.profile_avatar.delete(save=False)
        super().delete(*args, **kwargs)


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.FileField(upload_to="about_avatar", blank=True, null=True)
    avatar_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            existing = About.objects.get(pk=self.pk)
            if existing.about_avatar and existing.about_avatar != self.about_avatar:
                existing.about_avatar.delete(save=False)

        # Proceed with saving new file
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete avatar when instance is deleted
        if self.about_avatar:
            self.about_avatar.delete(save=False)
        super().delete(*args, **kwargs)


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    tech = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True, unique=True)
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
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_avatar = models.FileField(upload_to="contact_avatar", blank=True, null=True)
    avatar_link = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            existing = Contact.objects.get(pk=self.pk)
            if (
                existing.contact_avatar
                and existing.contact_avatar != self.contact_avatar
            ):
                existing.contact_avatar.delete(save=False)

        # Proceed with saving new file
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete avatar when instance is deleted
        if self.contact_avatar:
            self.contact_avatar.delete(save=False)
        super().delete(*args, **kwargs)
