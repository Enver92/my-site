from django.db import models
from django.urls import reverse

# Create your models here.
class Tag( models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    tag = models.ManyToManyField(Tag, help_text='Select tags for the post')

    def display_tags(self):
        return ', '.join([tag.name for tag in self.tag.all()[:3]] )
    display_tags.short_description = 'Tag'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this post.
        """
        return reverse('blog:post-detail', args=[str(self.id)])
