from django.contrib import admin
from .models import Posts

# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("post_id", "name", "describe", "image", "url", "content", "createDate", "url_name", "views", "status")