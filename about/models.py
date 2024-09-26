from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores information related to the 'About' section of the website.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
