from django.contrib import admin
from projects.models import Project

class Projects(admin.ModelAdmin):
    pass

admin.site.register(Project, Projects)

# Register your models here.
