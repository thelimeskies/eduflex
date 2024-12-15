from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from school.serializers import SchoolSerializer
from customer.serializers import ParentSerializer


class CustomUserDetailsSerializer(UserDetailsSerializer):
    """
    Custom user details serializer with conditional fields.
    """

    has_onboarded = serializers.BooleanField()
    school = SchoolSerializer(read_only=True)
    parent = ParentSerializer(read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "has_onboarded",
            "school",
            "parent",
        )
        read_only_fields = UserDetailsSerializer.Meta.read_only_fields + (
            "has_onboarded",
        )


class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom register serializer with additional fields.
    """

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    username = None  # Remove username field

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }


class CustomLoginSerializer(LoginSerializer):
    username = None  # Remove username field
