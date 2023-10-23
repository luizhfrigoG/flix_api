from django.urls import path

from . import views

urlpatterns = [
    path('reviews/', views.ReviewsCreateListView.as_view(),
         name='reviews-create-list'),
    path('reviews/<int:pk>/', views.ReviewsRetrieveUpdateDestroyView.as_view(),
         name='reviews-detail-view'),
]
