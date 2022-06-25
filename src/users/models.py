from allauth.account.models import EmailAddress
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    vocation = models.CharField(max_length=90, blank=True, null=True, verbose_name='Vocation')
    about_myself = models.CharField(max_length=290, blank=True, null=True,
                                    verbose_name='Let me tell you a few words about myself')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'
        ordering = ['-id']

    def __str__(self):
        return self.username

    def email_verified(self):
        if self.is_authenticated:
            result = EmailAddress.objects.filter(email=self.email)
            if len(result):
                return result[0].verified
        else:
            return False
