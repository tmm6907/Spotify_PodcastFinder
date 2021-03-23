from django.db import models
from django.views import generic

# Create your models here.
class Podcast(models.Model):
    name                = models.CharField(max_length = 50)
    publisher           = models.CharField(max_length = 25)
    description         = models.TextField()
    show_type           = models.CharField(max_length = 25)

class AuthToken(models.Model):
    user                = models.CharField(max_length = 12)
    created_at          = models.DateTimeField(auto_now_add=True)
    access_token        = models.CharField(max_length = 50)
    token_type          = models.CharField(max_length = 50)
    refresh_token       = models.CharField(max_length = 50)
    expires_in          = models.DateTimeField()

