from django.contrib import admin

from .models import Job  # . referencing loacl directory

admin.site.register(Job)