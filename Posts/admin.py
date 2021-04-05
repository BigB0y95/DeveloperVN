from django.contrib import admin
from .models import Posts

# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("Post_id", "name", "describe", "url", "content", "createDate", "status")