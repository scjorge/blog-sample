from djoser.serializers import UserSerializer


class UserProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = None
        exclude = [
            "id",
            "password",
            "is_active",
            "is_staff",
        ]
