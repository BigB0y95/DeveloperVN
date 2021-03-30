from django.contrib import admin
from .models import Lesson
# Register subject models.
@admin.register(Lesson)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("lesson_id", "subject_id", "name", "content", "url", "image", "time", "views", "dateCreate", "author", "url_name")
