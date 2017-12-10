# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class List(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Item(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
