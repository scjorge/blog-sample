from rest_framework.generics import (ListCreateAPIView, 
                                RetrieveUpdateDestroyAPIView)

from .models import Post, KeyWord
from .serializers import PostSerializer

        
class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetriveUpdatePost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer