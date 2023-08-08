from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadFile(models.Model):
    name=models.CharField(max_length=200, null=True)
    user_id=models.CharField(max_length=200, null=True)
    title=models.CharField('Title', max_length=50, null=True)
    file=models.FileField(null=True) #upload_to='media/'
    doctype=models.CharField('Document Type', max_length=50, null=True)
    description=models.TextField('Description', null=True)
    permissions=models.CharField('Permission', max_length=50, null=True)
    upload_date=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title