from django.contrib import admin
from home.models import *
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
admin.site.register(Skill)

# Register your models here.
