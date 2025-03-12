from django.contrib import admin
from forum.models import PostCategory, Post

admin.site.register(Post)
admin.site.register(PostCategory)
