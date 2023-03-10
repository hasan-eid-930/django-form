# Generated by Django 4.1.7 on 2023-03-10 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_remove_person_id_alter_person_file_alter_person_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='file',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='images/')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.person')),
            ],
        ),
    ]