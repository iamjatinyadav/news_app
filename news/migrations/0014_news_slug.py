# Generated by Django 3.1 on 2022-09-06 04:14

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_remove_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['heading']),
        ),
    ]
