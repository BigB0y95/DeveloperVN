from django.contrib import admin
from .models import Course

# Register subject models.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "name", "about", "content", "image", "dateCreate", "status")
