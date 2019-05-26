from django.urls import path
from contactsRest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('albums/', views.AlbumList.as_view()),
  path('addAlbum/', views.AddAlbum.as_view()),
  path('addTrack/', views.AddTrack.as_view()),
  path('tracks/', views.TrackList.as_view()),
  path('tracks/<search>', views.TrackList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)