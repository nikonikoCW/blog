from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class comment(models.Model):
    article = models.ForeignKey(article,related_name = 'article_comment',on_delete=models.CASCADE)
    detail = models.TextField()
    
    def __str__(self):
        return self.article
    
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    def __str__(self):
        return self.username
