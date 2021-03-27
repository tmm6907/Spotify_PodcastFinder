from django.db import models
from django.views import generic

# Create your models here.
class Podcast(models.Model):
    name                = models.CharField(max_length = 48)
    publisher           = models.CharField(max_length = 36)
    description         = models.TextField()
    show_type           = models.CharField(max_length = 12)

class AuthToken(models.Model):
    user                = models.CharField(max_length = 12)
    created_at          = models.DateTimeField(auto_now_add=True)
    access_token        = models.CharField(max_length = 48)
    token_type          = models.CharField(max_length = 48)
    refresh_token       = models.CharField(max_length = 48)
    expires_in          = models.DateTimeField()

