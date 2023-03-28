from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.TabularInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]
    list_display = ('username', 'profile')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
