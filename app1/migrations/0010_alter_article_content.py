# Generated by Django 4.1.7 on 2023-02-19 07:42

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_article_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=app1.models.get_blog),
        ),
    ]