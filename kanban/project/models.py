from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    class Meta:
        verbose_name_plural = "Projects"

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    project = models.ForeignKey(Project, related_name='project_member', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='members', on_delete=models.CASCADE)


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Statuses"

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name_plural = "Tasks"

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='task_author', on_delete=models.PROTECT)
    status = models.ForeignKey(Status, related_name='task_status', on_delete=models.PROTECT)
    project = models.ForeignKey(Project, related_name='task_projects', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
