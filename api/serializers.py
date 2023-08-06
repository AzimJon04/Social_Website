from django.contrib.auth.models import User
from rest_framework import serializers

from account.models import UserProfile
from publications.models import PostProfile


class UserPofileSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'first_name',
            'last_name',
            'phone_number',
            'telegram_link',
            'image',
            'last_login_ip',
            'follows',
            'created_at',
            )
        model = UserProfile


class PostProfileSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'title',
            'post',
            'comment',
            'user_like',
            'user_dislike',
            'created_at',
        )
        model = PostProfile


class UserCreateSrerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'password1',
            'password2',

        )
        model = User
