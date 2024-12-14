from rest_framework import serializers
from .models import School, SchoolCategory, SchoolClass


class SchoolOnboardingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    phone = serializers.CharField(max_length=15)
    email = serializers.EmailField(required=False, allow_null=True)
    website = serializers.URLField(required=False, allow_null=True)
    logo = serializers.ImageField(required=False, allow_null=True)
    categories = serializers.ListField(
        child=serializers.ChoiceField(choices=SchoolCategory.choices),
        allow_empty=False,
        help_text="Select school categories (e.g., Primary, Junior Secondary, Senior Secondary)",
    )

    def validate_categories(self, value):
        """
        Validates that at least one category is selected.
        """
        if not value:
            raise serializers.ValidationError("At least one category must be selected.")

        return value

    def validate(self, data):
        """
        Validates that email or phone is provided.
        """
        if not data.get("email") and not data.get("phone"):
            raise serializers.ValidationError("Either email or phone must be provided.")

        return data

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)

    def create(self, validated_data):
        """
        Creates a School instance and dynamically creates SchoolClass instances for the selected categories.
        """
        categories = validated_data.pop("categories")
        school = School.objects.create(**validated_data)

        # Dynamically create SchoolClass instances based on selected categories
        category_classes = {
            "Primary": [f"Primary {i}" for i in range(1, 7)],
            "Junior Secondary": [f"JSS {i}" for i in range(1, 4)],
            "Senior Secondary": [f"SSS {i}" for i in range(1, 4)],
        }

        for category in categories:
            if category in category_classes:
                for class_name in category_classes[category]:
                    SchoolClass.objects.create(
                        school=school,
                        category=category,
                        name=class_name,
                    )

        return school
