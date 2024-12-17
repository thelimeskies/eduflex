from ecraspay_django.services import EcraspayService
from ecraspay_django.models import Payment
from .models import Credit


def initiate_credit_payment(credit: Credit, customer_email: str):
    """
    Initiates payment for a credit application.
    """
    ecraspay_service = EcraspayService()

    # Generate unique payment reference
    payment_reference = f"CREDIT-{credit.id}"

    # Initiate checkout
    response = ecraspay_service.initiate_checkout(
        amount=credit.total_repayment_amount,
        reference=payment_reference,
        customer_name=f"{credit.parent.user.first_name} {credit.parent.user.last_name}",
        customer_email=customer_email,
        description="School fee credit repayment",
    )

    credit.payment = response["payment"]
    credit.save()

    return response["payment_link"]


from ecraspay_django.services import EcraspayService
from ecraspay_django.models import Payment
from .models import CreditRepayment, Credit


def verify_credit_payment(payment_reference):
    """
    Verify payment status for a given payment reference and update Credit status.
    """
    ecraspay_service = EcraspayService()

    try:
        payment = Payment.objects.get(payment_reference=payment_reference)
        response = ecraspay_service.verify_checkout(payment_reference)

        # Update Payment status
        if response["responseBody"]["status"] == "SUCCESSFUL":
            payment.status = "COMPLETED"
            payment.save()

            # Update CreditRepayment and Credit status
            credit = Credit.objects.filter(id=payment_reference.split("-")[1]).first()
            if credit:
                CreditRepayment.objects.create(
                    credit=credit,
                    payment=payment,
                    amount_paid=payment.amount,
                )
                credit.status = "REPAYMENT"
                credit.save()
            return True

        return False
    except Payment.DoesNotExist:
        return False
    except Exception:
        return False
