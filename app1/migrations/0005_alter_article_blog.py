# Generated by Django 4.1.7 on 2023-02-17 19:29

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_article_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(on_delete=models.SET(app1.models.get_blog), to='app1.blog'),
        ),
    ]
