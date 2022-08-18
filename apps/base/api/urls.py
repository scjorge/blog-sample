from django.urls import path

from .viewsets import ListCreatePost, RetriveUpdatePost

urlpatterns = [
    path("posts/", ListCreatePost.as_view(), name="create_post"),
    path("posts/<int:pk>/", RetriveUpdatePost.as_view(), name="create_post"),
]
