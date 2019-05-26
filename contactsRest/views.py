from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from contactsRest.models import Album
from contactsRest.serializers import AlbumSerializer
from collections import OrderedDict


class AlbumList(APIView):
  def get(self, request, format=None):
    albums = Album.objects.all()
    # albums = Album.objects.filter(album_name__icontains="um1")
    # albums = Album.objects.filter(tracks__duration__lte="120")
    serializer = AlbumSerializer(albums, many=True)
    # print(serializer.data)
    # return Response([{'name': 'album_name', 'name2': 'album1'}, ('artist', 'artist1')])
    return Response(serializer.data)
    