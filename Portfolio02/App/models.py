from django.db import models

# Create your models here.
class Janico(models.Model):
    about = models.TextField()
    name = models.CharField(max_length=200)
    profile = models.ImageField(upload_to="profile/")
    resume = models.FileField(upload_to="document/")

class Experience(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    duties = models.TextField()

class Projects(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    image = models.ImageField(upload_to="media/project_image", blank=True, null=True)
    stack = models.TextField()
    url = models.TextField(blank=True, null=True)
    
    def set_text_list(self, stack):
        self.stack = '\n'.join(stack)
        