from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Article(models.Model):
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