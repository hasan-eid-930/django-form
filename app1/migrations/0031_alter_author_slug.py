# Generated by Django 4.1.7 on 2023-03-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_alter_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='vf', unique=True),
        ),
    ]
