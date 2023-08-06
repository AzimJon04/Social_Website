from django.contrib import admin

from .models import PostProfile, PostComment
# Register your models here.


class PostProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'pk', 'created_at')


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('user_comment', 'id', 'created_at')


admin.site.register(PostProfile, PostProfileAdmin)
admin.site.register(PostComment, PostCommentAdmin)
