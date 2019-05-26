from rest_framework import serializers
from contactsRest.models import Album, Track

class TrackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Track
    fields = ('order', 'title', 'duration', 'album')    

class TrackSerializerWithId(serializers.ModelSerializer):
  class Meta:
    model = Track
    fields = ('id', 'order', 'title', 'duration', 'album')      

class AlbumSerializer(serializers.ModelSerializer):
  tracks = TrackSerializer(many=True, read_only=True)

  class Meta:
    model = Album
    fields = ('album_name', 'artist', 'tracks')

class TrackSerializerWithIdNoAlbumOrder(serializers.ModelSerializer):
  class Meta:
    model = Track
    fields = ('id', 'title', 'duration')      

class AlbumSerializerWithIdNoTrackAlbumOrder(serializers.ModelSerializer):
  tracks = TrackSerializerWithIdNoAlbumOrder(many=True, read_only=True)

  class Meta:
    model = Album
    fields = ('id', 'album_name', 'artist', 'tracks')    

