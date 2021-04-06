from django.contrib import admin
from .models import Course, Logo, Banner

# Register subject models.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "name", "about", "content", "image", "dateCreate", "status")

# Register logo models.
@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ("logo_id", "image", "createDate", "status")

# Register banner models.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("banner_id", "image", "createDate", "status")