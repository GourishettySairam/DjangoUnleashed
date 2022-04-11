from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config. ')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # order the instances by name

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse(
            'organizer_tag_update', kwargs={'slug': self.slug}
        )
    
    def get_delete_url(self):
        return reverse(
            'organizer_tag_delete', kwargs={'slug': self.slug}
        )

class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)   # index automatically in the database
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config. ')   #unique fields are automatically indexed
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)

    # Each startup will have multiple tags, 
    # and each tag may belong to multiple startups. 
    # This is a many-to-many relationship. 
    # Similarly, each blog post will be 
    # associated with tags via a many-to-many relationship
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
    
    def get_absolute_url(self):
        return reverse('organizer_startup_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'organizer_startup_update', kwargs={'slug': self.slug}
        )
    
    def get_delete_url(self):
        return reverse(
            'organizer_startup_delete', kwargs={'slug': self.slug}
        )

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)

    #  A one-to-many relationship pointing news links to startups
    #  A news link may belong to only one startup, 
    #  but a startup may have multiple news links, 
    #  meaning we seek to create a one-to-many relationship. 
    #  A news link points at a startup: 
    #  a news link has a foreign key to a startup.
    startup = models.ForeignKey(Startup, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{}:{}".format(self.startup, self.title)

    class Meta:
        verbose_name = "news article"   # to change name of class from news link to news article
        ordering = ["-pub_date"]
        get_latest_by = "pub_date"

    def get_absolute_url(self):
        return self.startup.get_absolute_url()
    
    def get_update_url(self):
        return reverse(
            'organizer_newslink_update',
            kwargs={'pk': self.pk}
        )
    
    def get_delete_url(self):
        return reverse(
            'organizer_newslink_delete',
            kwargs={'pk': self.pk}
        )