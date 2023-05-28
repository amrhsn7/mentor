# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Mentor,Session,Student,User 

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(User)