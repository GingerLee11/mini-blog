from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser

@admin.register(BlogUser)
class CustomUserAdmin(UserAdmin):
    model = BlogUser
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'last_login',
        )}),
        ('Additional Info', {'fields': (
            ('first_name', 'last_name'),
            'date_born',
            'short_bio',
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (None, {
        'fields': ('username', 'password1', 'password2'),
        'classes': ('wide',)
        }),
    )
    list_display = ('username', 'is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('last_login',)


