# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

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

class Comments(models.Model):
    feed         = models.ForeignKey(Feeds, related_name='details', on_delete=models.CASCADE)
    username     = models.ForeignKey(AppUser, related_name='details', on_delete=models.CASCADE)
    comment      = models.CharField(max_length=255) 
    comment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.feed.title + " by " + self.username.email
    


class Like(models.Model):
    user = models.ForeignKey(AppUser, related_name='likes', on_delete=models.CASCADE)
    feed = models.ForeignKey(Feeds, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return self.feed.title + " by " + self.user.email
