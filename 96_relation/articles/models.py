from django.db import models
<<<<<<< HEAD
from django.conf import settings
=======
from django.db.models.deletion import CASCADE
>>>>>>> fdb1a7bf510986878a22a39d23404433d2e59c6d

# Create your models here.

class Article(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
=======
    # id = 
    # pk = 
    title = models.CharField(max_length=100)
    content = models.TextField()
    # comment_set =

class Comment(models.Model):
    # id = 
    # pk =
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 
>>>>>>> fdb1a7bf510986878a22a39d23404433d2e59c6d
