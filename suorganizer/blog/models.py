from django.db import models
from organizer.models import Startup, Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, 
                help_text='A label for URL config',
                unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(
        'date_published',
        auto_now_add=True   #  automatically set to the current date the ﬁrst time it is submitted to the database
    )

    # Finally, we want to be able to write blog posts about startups. 
    # Each blog post may be about multiple startups, 
    # and each startup may be written about multiple times, 
    # another many-to-many relationship
    tags = models.ManyToManyField(
        Tag, 
        related_name='blog_posts'
    )
    startups = models.ManyToManyField(
        Startup, 
        related_name='blog_posts'
    )

    def __str__(self):
        return "{} on {}".format(
            self.title, 
            self.pub_date.strftime("%Y-%m-%d")
        )
