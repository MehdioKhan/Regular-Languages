from django.db import models


class Contact(models.Model):
    message = models.TextField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=False, null=False)
    date_time = models.DateTimeField(auto_now=True)