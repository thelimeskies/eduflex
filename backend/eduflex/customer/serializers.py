from rest_framework import serializers

from .models import Parents, Student, ParentKYC, ParentIDCategory


class ParentKYCSerializer(serializers.Serializer):
    annual_income = serializers.DecimalField(max_digits=10, decimal_places=2)
    employer = serializers.CharField(max_length=255)
    designation = serializers.CharField(max_length=255)
    bank_account_statement = serializers.FileField(
        help_text="Upload for 12 months.",
    )
    id_type = serializers.ChoiceField(choices=ParentIDCategory.choices)
    id_number = serializers.CharField(max_length=50)
    id_front = serializers.FileField(required=False)
    id_back = serializers.FileField(required=False)

    def validate(self, data):
        """
        Validates that id_type is provided.
        """
        if not data.get("id_type"):
            raise serializers.ValidationError("ID type must be provided.")

        return data

    def create(self, validated_data):
        return ParentKYC.objects.create(**validated_data)


class ParentOnboardingSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    address = serializers.CharField()
    occupation = serializers.CharField(max_length=255)
    kyc = ParentKYCSerializer()

    def validate(self, data):
        """
        Validates that first_name, last_name, and phone are provided.
        """
        if (
            not data.get("first_name")
            or not data.get("last_name")
            or not data.get("phone")
        ):
            raise serializers.ValidationError(
                "First name, last name, and phone must be provided."
            )

        return data
