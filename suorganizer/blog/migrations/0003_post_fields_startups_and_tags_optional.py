# Generated by Django 3.1.5 on 2022-04-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_unique_together_slug_startup'),
        ('blog', '0002_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Startup'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Tag'),
        ),
    ]