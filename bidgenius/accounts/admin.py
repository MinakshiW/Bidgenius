from .models import User, City
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

class UserAdmin(BaseUserAdmin):
    # Specify the fields to be used in displaying the User model.
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register your models here.
admin.site.register(City)
admin.site.register(User, UserAdmin)

