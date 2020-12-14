from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return f"{self.user}"

    #
    # Signal
    #
    @receiver(post_save, sender=get_user_model())
    def manage_user_profile(sender, instance, created, **kwargs):
        try:
            my_profile = instance.profile
            my_profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=instance)