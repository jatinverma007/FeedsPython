# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Comments, Feeds, Like

admin.site.register(Feeds)
admin.site.register(Like)
admin.site.register(Comments)
