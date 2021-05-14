from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class twitter(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    image = CloudinaryField('image',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
