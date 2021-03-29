from django.contrib import admin
from .models import Subjects

# Register subject models.
@admin.register(Subjects)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("subject_id", "course_id", "name", "dateCreate", "totalVisits")
