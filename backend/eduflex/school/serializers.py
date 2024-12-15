from rest_framework import serializers
from .models import School, SchoolCategory, SchoolClass, SchoolFee, Term


from django.db import transaction


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
        Ensure all categories are valid and prevent duplicates.
        """
        if not isinstance(value, list):
            raise serializers.ValidationError("Categories must be provided as a list.")

        if len(set(value)) != len(value):
            raise serializers.ValidationError("Duplicate categories are not allowed.")

        invalid_choices = [item for item in value if item not in SchoolCategory.values]
        if invalid_choices:
            raise serializers.ValidationError(
                f"Invalid category choices: {', '.join(invalid_choices)}"
            )

        return value

    def validate(self, data):
        """
        Validates that email or phone is provided.
        """
        if not data.get("email") and not data.get("phone"):
            raise serializers.ValidationError("Either email or phone must be provided.")

        return data

    def create(self, validated_data):
        """
        Creates a School instance and dynamically creates SchoolClass instances for the selected categories.
        """
        # Extract categories from validated_data since it's not part of the School model
        categories = validated_data.pop("categories")

        with transaction.atomic():
            # Create the School instance
            school = School.objects.create(
                admin=self.context["request"].user, **validated_data
            )

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


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class SchoolCategorySerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=SchoolCategory.choices)
    classes = serializers.ListField(child=serializers.CharField())


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = "__all__"


class SchoolFeeSerializer(serializers.Serializer):
    school_class_id = serializers.UUIDField()
    school_class = SchoolClassSerializer(read_only=True)
    term = serializers.ChoiceField(choices=Term.choices)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_school_class(self, value):
        """
        Validates that the school class exists.
        """
        try:
            school_class = SchoolClass.objects.get(id=value)
        except SchoolClass.DoesNotExist:
            raise serializers.ValidationError("Invalid school class.")

        return school_class

    def validate(self, data):
        """
        Validates that the fee amount is greater than zero.
        """
        if data["amount"] <= 0:
            raise serializers.ValidationError("Fee amount must be greater than zero.")

        return data

    def create(self, validated_data):
        return SchoolFee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)
        instance.save()
        return instance
