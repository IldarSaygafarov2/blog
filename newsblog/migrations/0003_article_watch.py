# Generated by Django 4.0.4 on 2022-05-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0002_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='watch',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
