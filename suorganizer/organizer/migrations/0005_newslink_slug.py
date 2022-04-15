# Generated by Django 3.1.5 on 2022-04-15 07:49

from email.policy import default
from django.db import migrations, models
from django.utils.text import slugify

from suorganizer.organizer.models import NewsLink

SLUG_LENGTH = 63

def add_slug_data(apps, schema_editor):
    NewsLink = apps.get_model('organizer', 'NewsLink')  
    query = NewsLink.objects.all()
    for newslink in query:
        expected_slug = slugify(newslink.title)
        rivals = (
            NewsLink.objects.filter(
                startup=newslink.startup,
                slug__startswith=expected_slug
            ).count()
        )

        if rivals > 0:
            str_len = (
                SLUG_LENGTH - len(str(rivals))
            )
            newslink.slug = "{}-{}".format(
                expected_slug[:str_len - 1],
                rivals + 1
            )
        else:
            newslink.slug = expected_slug
        
        newslink.save()

def remove_slug_data(apps, schema_editor):
    NewsLink = apps.get_model('organizer', 'NewsLink')
    NewsLink.objects.update(slug='')



class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0004_newslink_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslink',
            name='slug',
            field=models.SlugField(
                max_length=SLUG_LENGTH,
                default=''
            )
        ),
        migrations.RunPython(
            add_slug_data,
            reverse_code=remove_slug_data
        ),
        migrations.AlterField(
            model_name='newslink',
            name='slug',
            field=models.SlugField(
                max_length=SLUG_LENGTH
            )
        )
    ]
