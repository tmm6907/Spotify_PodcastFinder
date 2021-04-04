from django.db import models

# Create your models here.

class AuthToken(models.Model):
    user                = models.CharField(max_length = 12)
    created_at          = models.DateTimeField(auto_now_add=True)
    access_token        = models.CharField(max_length = 48)
    token_type          = models.CharField(max_length = 48)
    refresh_token       = models.CharField(max_length = 48)
    expires_in          = models.DateTimeField()

