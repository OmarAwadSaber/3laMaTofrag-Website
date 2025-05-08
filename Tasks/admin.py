from django.contrib import admin
from .models import Task, customUser


# Register your models here.
admin.site.register(customUser)
admin.site.register(Task)