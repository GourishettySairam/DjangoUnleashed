# Generated by Django 3.1.5 on 2022-04-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together={('slug', 'startup')},
        ),
    ]
