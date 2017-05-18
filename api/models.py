from django.db import models

class Track(models.Model):
    title           = models.CharField(max_length=255, null=True)
    image_path      = models.ImageField(upload_to='uploads', null=True)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)

    def output(self):
        track = {
            'id': self.id,
            'title': self.title,
            'image_path': self.image_path.name,
            'date_created': str(self.date_created),
            'date_updated': str(self.date_updated)
        }
        return track

    def keys(self):
        for field in self._meta.fields:
            print(field.name)

    def __str__(self):
        return self.title

class Set(models.Model):
    title           = models.CharField(max_length=255, null=True)
    tracks          = models.ManyToManyField(Track, through='TrackPosition')
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)

    def output(self, id):

        trackAssignments = TrackPosition.objects.filter(set=Set.objects.get(id=id))
        tracks = {}
        # Loop
        for trackAssignment in trackAssignments:
            track = Track.objects.get(id=trackAssignment.track.id)
            tracks[trackAssignment.position] = {
                'id': track.id,
                'title': track.title,
                'image_path': track.image_path.name,
                'date_created': track.date_created,
                'date_updated': track.date_updated,
            }
        #  End Loop
        set = {
            'title': self.title,
            'tracks': tracks,
            'date_created': str(self.date_created),
            'date_updated': str(self.date_updated)
        }
        return set

    def keys(self):
        for field in self._meta.fields:
            print(field.name)

    def __str__(self):
        return self.title

class Setlist(models.Model):
    title           = models.CharField(max_length=255, null=True)
    sets            = models.ManyToManyField(Set, through='SetlistPosition')
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)


    def output(self, setlist_id):
        # setlist = Setlist.objects.get(id=setlist_id)

        slps = SetlistPosition.objects.filter(setlist=Setlist.objects.get(id=setlist_id))

        sets = {}

        for slp in slps:
            trackAssignments = TrackPosition.objects.filter(set=Set.objects.get(id=slp.set.id))
            tracks = {}
            # Loop
            for trackAssignment in trackAssignments:
                track = Track.objects.get(id=trackAssignment.track.id)
                tracks[trackAssignment.position] = {
                    'id': track.id,
                    'title': track.title,
                    'image_path': track.image_path.name,
                    'date_created': track.date_created,
                    'date_updated': track.date_updated,
                }
            #  End Loop

            setInfo = {
                # 'title': self.title,
                'tracks': tracks,
            }

            sets[slp.position] = { 'cycles': slp.cycles, 'set': setInfo }

        setlistInfo = {
            'id': self.id,
            'title': self.title,
            'sets': sets,
        }
        return setlistInfo

    def keys(self):
        for field in self._meta.fields:
            print(field.name)

    def __str__(self):
        return self.title

class TrackPosition(models.Model):
    track           = models.ForeignKey(Track, on_delete=models.CASCADE)
    set             = models.ForeignKey(Set, on_delete=models.CASCADE)
    position        = models.IntegerField()
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)

    def keys(self):
        for field in self._meta.fields:
            print(field.name)

    def __str__(self):
        return self.set.title + '[' + str(self.position) + ']: ' + self.track.title

class SetlistPosition(models.Model):
    setlist         = models.ForeignKey(Setlist, on_delete=models.CASCADE)
    set             = models.ForeignKey(Set, on_delete=models.CASCADE)
    position        = models.IntegerField()
    cycles          = models.IntegerField()
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)

    def keys(self):
        for field in self._meta.fields:
            print(field.name)
    def __str__(self):
        return self.setlist.title + '[' + str(self.position) + ']: ' + self.set.title
