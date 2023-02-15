from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BlogPost
# Register your models here.


class CustomUserAdmin(UserAdmin):
    filter_horizontal=( )
    list_display = ('email','username', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    ordering = ("-date_joined",)
    fieldsets =()
    list_filter= ()
    # search_fields= ('role',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BlogPost)
