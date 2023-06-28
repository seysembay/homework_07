from django.contrib import admin

from .models import Project
from .models import Member
from .models import Task
from .models import Status


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    list_display_links = "id", "name"


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = "id", "project_id", "user_id"


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "author_id"
    list_display_links = "id", "name"