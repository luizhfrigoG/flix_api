from django.contrib import admin
from django.urls import path

from actors.views import ActorCreateListView, ActorRetrieverUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import (ReviewsCreateListView,
                           ReviewsRetrieveUpdateDestroyView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(),
         name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetrieverUpdateDestroyView.as_view(),
         name='actors-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='movies-detail-view'),

    path('reviews/', ReviewsCreateListView.as_view(),
         name='reviews-create-list'),
    path('reviews/<int:pk>/', ReviewsRetrieveUpdateDestroyView.as_view(),
         name='reviews-detail-view'),

]
