from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from cases.models import *
# Register your models here.

@admin.register(WebsiteUser)
class WebsiteUserAdmin(UserAdmin):
    # Fields to display in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Fields searchable in admin
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Default ordering
    ordering = ('username',)

    # Fieldsets for user detail/edit page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(Case)
admin.site.register(Lawyer)
admin.site.register(Client)

# change in the dashboard
