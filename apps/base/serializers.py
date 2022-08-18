from rest_framework import serializers

from .models import Post, KeyWord


class PostSerializer(serializers.ModelSerializer):
    class KeyWordSerializer2(serializers.Serializer):
        name = serializers.CharField()

    keyword = KeyWordSerializer2(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "subtitle",
            "type_post",
            "content",
            "status",
            "keyword",
        ]

    def create(self, validated_data):
        keyword_data = validated_data.pop("keyword")
        mapping_keyword = list(map(lambda x: dict(x), keyword_data))

        post = Post.objects.create(
            title=validated_data["title"],
            subtitle=validated_data["subtitle"],
            type_post=validated_data["type_post"],
            content=validated_data["content"],
            status=validated_data["status"],
        )
        keywords_list = []
        for item in mapping_keyword:
            k, _ = KeyWord.objects.get_or_create(name=item["name"])
            keywords_list.append(k.id)

        for k in keywords_list:
            post.keyword.add(k)
        return post

    def update(self, instance, validated_data):
        keyword_data = validated_data.pop("keyword")
        mapping_keyword = list(map(lambda x: dict(x), keyword_data))
        keywords_list = []
        instance.keyword.set([None])

        for item in mapping_keyword:
            k, _ = KeyWord.objects.get_or_create(name=item["name"])
            keywords_list.append(k.id)

        for k in keywords_list:
            instance.keyword.add(k)

        return super().update(instance, validated_data)
