from django.db import models

# Create your models here.
show_types = (
    ('shows', 'shows'),
    ('episodes', 'episodes'),
)
class Show(models.Model):
    show_id             = models.CharField(max_length = 25)
    name                = models.CharField(max_length = 48)
    description         = models.TextField()
    languages           = models.TextField(default = 'NULL')
    show_type           = models.CharField(max_length = 8, choices = show_types)

# class Episode(models.Model):
#     show_id             = models.CharField(max_length = 25)
#     name                = models.CharField(max_length = 48)
#     description         = models.TextField()
#     show_type           = models.CharField(max_length = 8, choices = show_types)
