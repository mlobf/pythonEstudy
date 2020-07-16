from django.db import models

class Post(models.Model):
    title = models.CharField(max_lenght=50)
    content = models.TextField()
    date = models.DateField()


