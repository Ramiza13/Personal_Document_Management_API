# Generated by Django 4.2.3 on 2023-08-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_uploadfile_name_uploadfile_upload_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]