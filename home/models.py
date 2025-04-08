# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Plot(models.Model):

    #__Plot_FIELDS__
    number = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    cadastral_number = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    additional_phone = models.CharField(max_length=255, null=True, blank=True)
    person = models.CharField(max_length=255, null=True, blank=True)

    #__Plot_FIELDS__END

    class Meta:
        verbose_name        = _("Plot")
        verbose_name_plural = _("Plot")


class Plotgroup(models.Model):

    #__Plotgroup_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    plots = models.CharField(max_length=255, null=True, blank=True)

    #__Plotgroup_FIELDS__END

    class Meta:
        verbose_name        = _("Plotgroup")
        verbose_name_plural = _("Plotgroup")


class Person(models.Model):

    #__Person_FIELDS__
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    residence_address = models.CharField(max_length=255, null=True, blank=True)
    mailing_address = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    is_member = models.BooleanField()
    voting_weight = models.IntegerField(null=True, blank=True)
    ownership_share = models.IntegerField(null=True, blank=True)
    can_vote = models.BooleanField()
    can_vote_online = models.BooleanField()

    #__Person_FIELDS__END

    class Meta:
        verbose_name        = _("Person")
        verbose_name_plural = _("Person")



#__MODELS__END
