from django.db import models
from django_quill.fields import QuillField


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = QuillField()
    image = models.ImageField(upload_to='media/images')
    slug = models.SlugField(unique=True)
    publish_date = models.DateTimeField()
    status = models.BooleanField(default=0)

    class Meta:
        ordering = ['-publish_date']


    def __str__(self):
        return self.title