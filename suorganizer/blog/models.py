from django.db import models
from organizer.models import Startup, Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()

    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup
