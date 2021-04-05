from django.contrib import admin
from .models import Info_Account, Sponsor
# Register your models here.

@admin.register(Info_Account)
class Infor_Account_Admin(admin.ModelAdmin):
    list_display = ("account_id", "name", "image", "account", "recipients", "dateCreate", "status")

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("sponsor_id", "sender","account", "money", "message", "sentDate", "status")