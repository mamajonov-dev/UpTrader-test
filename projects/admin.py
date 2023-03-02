from django.contrib import admin

from .models import ProjectsModel, Tags, Reviews

admin.site.register(ProjectsModel)

admin.site.register(Tags)
admin.site.register(Reviews)