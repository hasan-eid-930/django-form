# Generated by Django 4.1.7 on 2023-02-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_article_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='num',
        ),
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
    ]