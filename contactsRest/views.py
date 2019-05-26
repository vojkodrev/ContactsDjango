from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from contactsRest.models import Album, Track
from contactsRest.serializers import AlbumSerializer, TrackSerializerWithId, AlbumSerializerWithIdNoTrackAlbumOrder, TrackSerializer
from collections import OrderedDict


class AlbumList(APIView):
  def get(self, request, format=None):
    albums = Album.objects.all()
    # albums = Album.objects.filter(album_name__icontains="um1")
    # albums = Album.objects.filter(tracks__duration__lte="120")
    serializer = AlbumSerializerWithIdNoTrackAlbumOrder(albums, many=True)
    # print(serializer.data)
    # return Response([{'name': 'album_name', 'name2': 'album1'}, ('artist', 'artist1')])
    return Response(serializer.data)

class TrackList(APIView):
  def get(self, request, search="", format=None):
    albums = Track.objects.filter(title__icontains=search)
    serializer = TrackSerializerWithId(albums, many=True)
    return Response(serializer.data)    


class AddAlbum(APIView):
  def post(self, request, format=None):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class AddTrack(APIView):

  def post(self, request, format=None):
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

# class SnippetDetail(APIView):
#   """
#   Retrieve, update or delete a snippet instance.
#   """
#   def get_object(self, pk):
#     try:
#       return Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#       raise Http404

#   def get(self, request, pk, format=None):
#     snippet = self.get_object(pk)
#     serializer = SnippetSerializer(snippet)
#     return Response(serializer.data)

#   def put(self, request, pk, format=None):
#     snippet = self.get_object(pk)
#     serializer = SnippetSerializer(snippet, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, pk, format=None):
#     snippet = self.get_object(pk)
#     snippet.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)    
    