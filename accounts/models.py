from django.db import models
from django.contrib.auth.models import User
from photo.models import city
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256, default=None, null=True, blank=True, verbose_name="Номер телефона")
    user_city = models.ManyToManyField(city, blank=True, default=None)

    def get_city(self):
        return ",".join([str(p) for p in self.user_city.all()])

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()