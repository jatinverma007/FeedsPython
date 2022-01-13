# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from register.models import AppUser

class Feeds(models.Model):
    profile    = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    feed_type  = models.PositiveIntegerField()
    title      = models.CharField(max_length=200)
    desc       = models.CharField(max_length=500)
    link       = models.CharField(max_length=1024)
    # image      = models.ImageField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title