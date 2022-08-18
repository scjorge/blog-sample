from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Post
from .serializers import PostSerializer


class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    # on productions we be used for cache data
    
    #@method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class RetriveUpdatePost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
