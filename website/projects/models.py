from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")


class Work(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")