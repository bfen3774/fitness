from django.contrib import admin
from .models import Plan, Progress

admin.site.register(Plan)

class ProgressInline(admin.TabularInline):
    model = Plan
# Register your models here.
