from django.contrib import admin
from home.models import Position, Project, Education
"""
class Positions(admin.ModelAdmin):
    pass
class Projects(admin.ModelAdmin):
    pass
class Educations(admin.ModelAdmin):
    pass */
"""
admin.site.register(Position)
admin.site.register(Project)
admin.site.register(Education)


# Register your models here.
