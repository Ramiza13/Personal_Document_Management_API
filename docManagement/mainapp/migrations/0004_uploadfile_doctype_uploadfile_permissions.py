# Generated by Django 4.2.3 on 2023-08-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='doctype',
            field=models.CharField(max_length=50, null=True, verbose_name='Document Type'),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='permissions',
            field=models.CharField(max_length=50, null=True, verbose_name='Permission'),
        ),
    ]
