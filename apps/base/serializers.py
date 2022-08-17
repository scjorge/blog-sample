from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, KeyWord


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "subtitle",
            "type_post",
            "content",
            "status",
        ]
        


class KeyWordSerializer1(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = [
            "name",
        ]


class KeyWordSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_keyword_set_format(self, keyword):
        if not isinstance(keyword, dict):
            raise ValidationError({"errors":"List must be contain a JSON with 'name' as Keys"})

        if not "name" in keyword.keys():
            raise ValidationError({"errors":"List must be contain a JSON with 'name' as Keys"})

        if not isinstance(keyword["name"], str):
            raise ValidationError({"errors":"List must be contain a JSON with sting values"})

        return keyword


    def validate_keyworda_set(self, keyword):
        keyword = list(filter(self.validate_keyword_set_format, keyword))
        if len(keyword) == 0:
            raise ValidationError({"errors":"List must be contain a JSON with 'name' as Keys"})
        return keyword