from django.contrib import admin
from home.models import Position, Project, Education

class Positions(admin.ModelAdmin):
    pass
class Projects(admin.ModelAdmin):
    pass
class Educations(admin.ModelAdmin):
    pass

admin.site.register(Position,  Positions)
admin.site.register(Project,   Projects)
admin.site.register(Education, Educations)


# Register your models here.
