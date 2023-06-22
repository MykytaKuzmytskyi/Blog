from django.contrib import admin
from django.contrib.auth import get_user_model

from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(get_user_model())
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
