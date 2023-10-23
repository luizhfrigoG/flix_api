from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewsSerializer


class ReviewsCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
