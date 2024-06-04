from django.contrib import admin

from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'featured_image', 'description', 'like', 'created_by', 'is_deleted')
admin.site.register(Post, PostAdmin)
