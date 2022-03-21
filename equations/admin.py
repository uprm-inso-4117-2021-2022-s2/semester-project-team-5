from django.contrib import admin

from .models import Question, Solution

# Register your models here.
admin.site.register(Question)
admin.site.register(Solution)
