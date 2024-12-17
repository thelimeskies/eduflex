from rest_framework import serializers

from .models import Credit, CreditRepayment, PaymentSchedule


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = "__all__"


class CreditRepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditRepayment
        fields = "__all__"


class PaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSchedule
        fields = "__all__"
