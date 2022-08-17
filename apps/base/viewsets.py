from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import Post, KeyWord
from .serializers import PostSerializer, KeyWordSerializer, KeyWordSerializer1


class CreatePost(APIView):

    def post(self, request):
        post_serializer = PostSerializer(data=request.data)
        keyword_serializer = KeyWordSerializer(data=request.data)

        post_serializer.is_valid(raise_exception=True)
        keyword_serializer.is_valid(raise_exception=True)

        keywords = request.data["keyword_set"]
        keywords_list = []

        for keyword in keywords:
            k, _ = KeyWord.objects.get_or_create(keyword_set=keyword['name'])
            keywords_list.append(k.id)

        post = post_serializer.save()
        list(map(lambda x: post.keyword.add(x), keywords_list))        
        
        post_serializer.data['keyword_set'] = keywords

        return Response([post_serializer.data, keyword_serializer.data], status=status.HTTP_201_CREATED)


        
class CreatePost1(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        post_serializer = self.get_serializer(data=request.data)
        post_serializer.is_valid(raise_exception=True)

        try:
            keyword = request.data.pop("keyword_set")
        except KeyError:
            return Response({"keyword_set":["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        keywords_list = []

        with transaction.atomic():
            for item in keyword:
                KeyWordSerializer(data=item).is_valid(raise_exception=True)
                k, _ = KeyWord.objects.get_or_create(name=item)
                keywords_list.append(k.id)

            post = post_serializer.save()
            for k in keywords_list:
                post.keyword.add(k)


        return Response(post_serializer.data, status=status.HTTP_201_CREATED)