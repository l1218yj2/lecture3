from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments")
    content = models.CharField(max_length=40)
