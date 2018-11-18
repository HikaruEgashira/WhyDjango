from django.db import models
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    published = models.DateTimeField()
    body1 = models.TextField()
    body2 = models.TextField()
    body3 = models.TextField()
    body4 = models.TextField()

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

    def __str__(self):
        return self.title