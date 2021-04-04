from django.contrib import admin
from .models import Contact_User, Contact_Live

# Register Contact User models .
@admin.register(Contact_User)
class Contact_User_Admin(admin.ModelAdmin):
    list_display = ("contact_id", "contact_person", "mail", "phone", "content", "createDate", "status")
# Register Contact Live models .
@admin.register(Contact_Live)
class Contact_Live_Admin(admin.ModelAdmin):
    list_display = ("contact_live_id", "name", "content", "url", "icon", "createDate", "status")