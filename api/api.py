#from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Track
from api.models import Set
from api.models import Setlist
from api.models import TrackPosition


class TrackHandler(APIView):

    # /tracks/:id
    def get(self, request, track_id):
        track = Track.objects.get(id=track_id)
        return Response(track.output())

class SetHandler(APIView):

    # /sets/:id
    def get(self, request, set_id):
        set = Set.objects.get(id=set_id)
        return Response(set.output(id=set_id))

class SetlistHandler(APIView):

    # /setlists/:id
    def get(self, request, setlist_id):
        setlist = Setlist.objects.get(id=setlist_id)
        return Response(setlist.output(setlist_id=setlist_id))
