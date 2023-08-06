from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import UserProfile
# Register your models here.


admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


admin.site.unregister(Group)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'user_id')


admin.site.register(UserProfile, UserProfileAdmin)
