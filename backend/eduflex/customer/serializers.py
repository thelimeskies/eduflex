from rest_framework import serializers
from .models import Parents, Student, ParentKYC, ParentIDCategory
from django.contrib.auth import get_user_model

User = get_user_model()


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
        Validates that the phone number is unique.
        """
        if Parents.objects.filter(phone=data["phone"]).exists():
            raise serializers.ValidationError(
                "A parent with this phone number already exists."
            )

        return data

    def create(self, validated_data):
        kyc_data = validated_data.pop("kyc")
        parent = Parents.objects.create(
            user=self.context["request"].user, **validated_data
        )
        ParentKYC.objects.create(parent=parent, **kyc_data)

        return parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = [
            "id",
            "phone",
            "address",
            "occupation",
        ]


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "school_class",
            "school",
            "parent",
        ]


class ParentCreditAndCapacityScoreSerializer(serializers.Serializer):
    credit_score = serializers.IntegerField()
    capacity_score = serializers.IntegerField()
    credit_score_description = serializers.CharField()
    capacity_score_description = serializers.CharField()
    credit_score_recommendation = serializers.CharField()
    capacity_score_recommendation = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
