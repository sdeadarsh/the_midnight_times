# Generated by Django 4.2.13 on 2024-06-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_search_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='img',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]