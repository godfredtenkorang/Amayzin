from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    project_title = models.CharField(max_length=250)
    project_content = models.TextField()
    home_content = models.TextField()
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField('date published')
    
    class Meta:
        verbose_name_plural = 'project categories'
        ordering = ['-date_added',]

    def __str__(self):
        return self.name

class Project(models.Model):
    main_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='usproj-img')
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'projects'
        ordering = ['-date_added',]
        

class YouTube(models.Model):
    title = models.CharField(max_length=100)
    url = EmbedVideoField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'YouTube'
        ordering = ['-date_added',]

    def __str__(self):
        return self.title


class GalleryCategory(models.Model):
    image = models.ImageField(upload_to='gallery-image')
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    date_added = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = 'gallery categories'
        ordering = ['-date_added',]

    def __str__(self):
        return self.title


class Gallery(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='each_gallery_imgs')

    class Meta:
        verbose_name_plural = 'galleries'



class News(models.Model):
    image = models.ImageField(upload_to='news-image')
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'news'
        ordering = ['-date_posted',]

    def __str__(self):
        return self.title


class Sponsorship(models.Model):
    image = models.ImageField(upload_to='sponsorship-img')
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField()
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'sponsorships'

    def __str__(self):
        return self.name


class VolunteerApplication(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=225, null=True, blank=True)
    states = models.CharField(max_length=225, null=True, blank=True)
    zipcode = models.CharField(max_length=225)
    volunteer_position = models.CharField(max_length=50)
    volunteer_experience = models.TextField()
    volunteer_skills = models.CharField(max_length=225)
    training_and_decrees_received = models.CharField(max_length=300)
    reason_for_volunteer = models.TextField(null=True, blank=True)
    references = models.TextField()
    datetime_available = models.CharField(max_length=250)
    emergency_contact = models.CharField(max_length=300)
    criminal_conviction = models.CharField(
        max_length=300, null=True, blank=True)
    verified = models.CharField(max_length=3)
    signature = models.CharField(max_length=20)
    date = models.DateField()
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'volunteer appliction'
        ordering = ['-date',]
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} Application"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contact'
        ordering = ['-date_added']

    def __str__(self):
        return self.name
