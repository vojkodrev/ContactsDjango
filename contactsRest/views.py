from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from contactsRest.models import Album
from contactsRest.serializers import AlbumSerializer


class AlbumList(APIView):
  def get(self, request, format=None):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)
    