from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image = models.FilePathField(path="/website/art_collections/static/img")


class Work(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image = models.FilePathField(path="/website/art_collections/static/img")