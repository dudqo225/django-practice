from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    image = ProcessedImageField(upload_to='avatars',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 60})