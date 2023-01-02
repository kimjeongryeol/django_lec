from django.db import models

# Create your models here.
class MainContent(models.Model):
    title =  models.CharField(max_length=500)
    content = models.TextField()
    pub_date = models.DateTimeField('data published')