# Generated by Django 4.2.3 on 2023-08-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('file', models.FileField(upload_to='')),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
        ),
    ]
