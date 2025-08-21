from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static


# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile/picture')
    userCode = models.CharField(max_length=12 , null=True)

    def __str__(self):
        return self.user.username

    @property
    def image_url(self) -> str:
        if self.image and getattr(self.image, 'name', None):
            try:
                if self.image.storage.exists(self.image.name):
                    return self.image.url
            except Exception:
                pass
        return static('images/default.jpg')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Ensure that accessing instance.profile does not fail after user save
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance, username=instance.username)
