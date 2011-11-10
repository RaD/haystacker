# -*- coding: utf-8 -*-
# (c) 2011 Ruslan Popov <ruslan.popov@gmail.com>

from django.db import models

class Text(models.Model):
    desc = models.TextField()

    def __unicode__(self):
        return self.desc
