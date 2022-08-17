from django.urls import path

from .viewsets import CreatePost1

urlpatterns = [
    path('create/', CreatePost1.as_view(), name="create_post"),
]