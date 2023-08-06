from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# class User(AbstractUser):
#     image = models.ImageField(upload_to='users_images', blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    telegram_link = models.URLField(max_length=100, blank=True)
    image = models.ImageField(upload_to='users_images', blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.userprofile)
        user_profile.save()
