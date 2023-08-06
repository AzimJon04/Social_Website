from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from account.models import UserProfile, User
# Create your models here.


class PostComment(models.Model):
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_comment.username

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']


class PostProfile(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_post',
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=50, null=True)
    post = models.TextField(max_length=500)
    comment = models.ManyToManyField(
        PostComment,
        related_name='comment_post',
        blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    user_like = models.ManyToManyField(
        UserProfile,
        related_name='user_like',
        blank=True
        )
    user_dislike = models.ManyToManyField(
        UserProfile,
        related_name='user_dislike',
        blank=True,
        )

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return str(self.user.username) + "'s post"
