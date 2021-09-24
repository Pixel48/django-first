from typing import cast
from django.db import models
from django.conf import settings
from django.db.models.fields import DateField
from django.utils import timezone

class Post(models.Model):
  title = models.CharField(max_length=250)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title