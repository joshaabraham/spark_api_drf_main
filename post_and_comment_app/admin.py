from django.contrib import admin
from post_and_comment_app.models import Comment, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
