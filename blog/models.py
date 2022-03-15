from django.db import models
from extensions.utils import jalali_converter
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from tinymce.models import HTMLField


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    abstract = models.TextField(null=True)
    content = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='static/images', blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    publish_date = models.DateTimeField()
    status = models.BooleanField(default=0)

    class Meta:
        ordering = ['-publish_date']

    def jpublish(self):
        return jalali_converter(self.publish_date)

    def __str__(self):
        return self.title