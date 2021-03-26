from django.contrib import admin
from .models import Member
# Register your models here.
admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):  
    list_display = ("id", "email", "password", "birthday", "userName", "sex", "point", "dateCreate", "status", "activeCount")