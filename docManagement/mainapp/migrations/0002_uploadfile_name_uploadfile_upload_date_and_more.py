# Generated by Django 4.2.3 on 2023-08-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='user_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]