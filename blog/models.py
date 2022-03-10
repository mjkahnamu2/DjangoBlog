from django.db import models
from django_quill.fields import QuillField
from extensions.utils import jalali_converter


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = QuillField()
    image = models.ImageField(upload_to='static/images')
    slug = models.SlugField(unique=True, allow_unicode=True)
    publish_date = models.DateTimeField()
    status = models.BooleanField(default=0)

    class Meta:
        ordering = ['-publish_date']

    def jpublish(self):
        return jalali_converter(self.publish_date)

    def __str__(self):
        return self.title