# Generated by Django 4.1.7 on 2023-02-21 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_article_num_article_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='file',
        ),
    ]