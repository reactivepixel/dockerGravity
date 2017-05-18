from django.db import models

class Track(models.Model):
    title           = models.CharField(max_length=255)
    image_path      = models.ImageField()
    mime_type       = models.CharField(max_length=255)
    date_created    = models.DateField()
    date_updated    = models.DateField()

class Set(models.Model):
    title           = models.CharField(max_length=255)
    tracks          = models.ManyToManyField(Track, through='TrackPosition')
    date_created    = models.DateField()
    date_updated    = models.DateField()

class Setlist(models.Model):
    title           = models.CharField(max_length=255)
    sets            = models.ManyToManyField(Set)

class TrackPosition(models.Model):
    track           = models.ForeignKey(Track, on_delete=models.CASCADE)
    set             = models.ForeignKey(Set, on_delete=models.CASCADE)
    position        = models.IntegerField()
