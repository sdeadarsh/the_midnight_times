# Generated by Django 4.2.13 on 2024-06-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_search_api', '0005_alter_searchresult_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='img',
            field=models.URLField(blank=True, default='https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg', null=True),
        ),
    ]