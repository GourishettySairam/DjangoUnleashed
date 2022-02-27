from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config. ')

class Startup(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()

    # Each startup will have multiple tags, 
    # and each tag may belong to multiple startups. 
    # This is a many-to-many relationship. 
    # Similarly, each blog post will be 
    # associated with tags via a many-to-many relationship
    tags = models.ManyToManyField(Tag)

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField()

    #  A one-to-many relationship pointing news links to startups
    #  A news link may belong to only one startup, 
    #  but a startup may have multiple news links, 
    #  meaning we seek to create a one-to-many relationship. 
    #  A news link points at a startup: 
    #  a news link has a foreign key to a startup.
    startup = models.ForeignKey(Startup)





Each startup will have multiple tags, and each tag may belong to multiple startups. This is a many-to-many relationship. Similarly, each blog post will be associated with tags via a many-to-many relationship
Finally, we want to be able to write blog posts about startups. Each blog post may be about multiple startups, and each startup may be written about multiple times, another many-to-many relationship
