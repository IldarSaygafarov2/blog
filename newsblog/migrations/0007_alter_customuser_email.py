# Generated by Django 4.0.4 on 2022-06-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0006_customuser_username_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='None', max_length=254, null=True),
        ),
    ]