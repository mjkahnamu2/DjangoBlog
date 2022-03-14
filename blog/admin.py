from operator import mod
from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'jpublish', 'status')



admin.site.register(Post, PostAdmin)
