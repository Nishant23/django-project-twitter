# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from .validators import *
from django.urls import reverse

# def validate_content(value):
#     content = value
#     if content == "abc":
#         raise ValidationError("Content can't be ABC")
#     return super(Tweet, self).clean(*args, **kwargs )


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content = models.CharField(max_length=140, default="", validators=[validate_content])
    uodated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={'pk':self.pk})

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content can't be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs )
