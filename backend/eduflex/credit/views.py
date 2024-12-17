from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from . import serializers

from .models import Credit, CreditRepayment, PaymentSchedule
from .service import initiate_credit_payment, verify_credit_payment


class CreditView(views.APIView):
    serializer_class = serializers.CreditSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, parent_id):
        credits = Credit.objects.filter(parent_id=parent_id)
        if not credits:
            return Response(
                {"message": "No credits found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(credits, many=True)
        return Response(serializer.data)


class CreditRepaymentView(views.APIView):
    serializer_class = serializers.CreditRepaymentSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, credit_id):
        repayments = CreditRepayment.objects.filter(credit_id=credit_id)
        if not repayments:
            return Response(
                {"message": "No repayments found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(repayments, many=True)
        return Response(serializer.data)


class PaymentScheduleView(views.APIView):
    serializer_class = serializers.PaymentScheduleSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, credit_id):
        schedules = PaymentSchedule.objects.filter(credit_id=credit_id)
        if not schedules:
            return Response(
                {"message": "No schedules found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(schedules, many=True)
        return Response(serializer.data)


class CreditPaymentInitiationView(views.APIView):
    """
    API endpoint to initiate payment for a Credit.
    """

    def post(self, request, credit_id):
        try:
            credit = Credit.objects.get(id=credit_id)
            customer_email = request.user.email  # Assume user is logged in

            # Initiate payment and return checkout URL
            checkout_url = initiate_credit_payment(credit, customer_email)

            return Response({"checkout_url": checkout_url}, status=200)

        except Credit.DoesNotExist:
            return Response({"error": "Credit not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class CreditPaymentCallbackView(views.APIView):
    """
    API endpoint to handle payment callback for a Credit.
    """

    def post(self, request):
        try:
            payment_reference = request.data["payment_reference"]
            payment_status = request.data["status"]

            # Find the related credit by payment reference
            credit = Credit.objects.get(payment__reference=payment_reference)

            # Update credit status based on payment status
            if payment_status == "COMPLETED":
                credit.status = "APPROVED"
                credit.save()

            return Response({"message": "Payment callback successful"}, status=200)

        except Credit.DoesNotExist:
            return Response({"error": "Credit not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class PaymentVerificationPollingView(views.APIView):
    """
    API endpoint to poll and verify payment status.
    """

    def get(self, request, payment_reference):
        success = verify_credit_payment(payment_reference)

        if success:
            return Response({"status": "Payment verified successfully."}, status=200)
        return Response({"status": "Payment pending or failed."}, status=400)
