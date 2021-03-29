from django.db import models
from django.views import generic

show_choices = [
    'shows',
    'episodes',
]
# Create your models here.
class Show(models.Model):
    name                = models.CharField(max_length = 48)
    publisher           = models.CharField(max_length = 36)
    description         = models.TextField()
    show_type           = models.CharField(choices = show_choices)

class Episode(models.Model):
    episode_name        = models.CharField(max_length = 48)
    id                  = models.CharField(max_length = 36)
    description         = models.TextField()
    show_type           = models.CharField(choices = show_choices)

class AuthToken(models.Model):
    user                = models.CharField(max_length = 12)
    created_at          = models.DateTimeField(auto_now_add=True)
    access_token        = models.CharField(max_length = 48)
    token_type          = models.CharField(max_length = 48)
    refresh_token       = models.CharField(max_length = 48)
    expires_in          = models.DateTimeField()

