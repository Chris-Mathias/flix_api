from django.urls import path
from . import views


urlpatterns = [
    path("reviews/", views.ReviewListCreateView.as_view(), name='review-list-create'),
    path("reviews/<int:pk>/", views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
]
