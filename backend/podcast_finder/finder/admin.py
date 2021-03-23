from django.contrib import admin
from .models import Podcast, AuthToken
# Register your models here.
admin.site.register(Podcast)
admin.site.register(AuthToken)