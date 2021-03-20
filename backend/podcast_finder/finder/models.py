from django.db import models

# Create your models here.
class Podcast(models.Model):
    class Meta:
        name                = models.CharField(max_length=50)
        publisher           = models.CharField(max_length=25)
        description         = models.TextField()
        show_type           = models.CharField(max_length=25)
