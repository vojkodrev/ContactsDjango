from django.urls import path
from contactsRest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('albums/', views.AlbumList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)