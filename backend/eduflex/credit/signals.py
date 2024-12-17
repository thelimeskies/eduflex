from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import timedelta, date

from .models import Credit, PaymentSchedule, CreditStatus
from customer.models import ParentCreditCapacityScore
from school.models import Payments

from django.dispatch import receiver
from django.db.models.signals import post_save
from ecraspay_django.models import Payment
from .models import Credit, CreditRepayment


@receiver(post_save, sender=Credit)
def create_payment_schedule(sender, instance, created, **kwargs):
    """
    Create a repayment schedule dynamically when the credit is approved.
    The schedule will be split based on the parent's credit capacity score.
    """
    if not created and instance.status == CreditStatus.APPROVED:
        # Fetch parent's credit capacity
        capacity_score = ParentCreditCapacityScore.objects.filter(
            parent=instance.parent
        ).first()

        if not capacity_score:
            raise ValueError("Credit capacity score not found for this parent")

        total_amount = instance.total_repayment_amount
        max_installments = int(
            1 + (capacity_score.capacity_score / 100 * 5)
        )  # 1 to 6 installments
        installment_amount = round(total_amount / max_installments, 2)

        # Clear previous schedules
        instance.schedules.all().delete()

        # Create schedules
        today = date.today()
        for i in range(max_installments):
            due_date = today + timedelta(weeks=(i + 1) * 4)  # Monthly intervals
            PaymentSchedule.objects.create(
                credit=instance,
                due_date=due_date,
                amount=installment_amount,
                status=CreditStatus.PENDING,
            )


# Create payments for School when credit is accepted
@receiver(post_save, sender=Credit)
def create_school_payments(sender, instance, created, **kwargs):
    if not created and instance.status == CreditStatus.APPROVED:
        total_amount = instance.total_amount
        school = instance.school
        child = instance.child
        Payments.objects.create(
            school=school,
            amount=total_amount,
            status=CreditStatus.PENDING,
            credit=instance,
            child=child,
        )


@receiver(post_save, sender=Payment)
def link_credit_repayment(sender, instance, created, **kwargs):
    """
    Signal to create a CreditRepayment instance when a Payment status is COMPLETED.
    """
    if instance.status == "COMPLETED":
        try:
            # Find the related credit by payment reference
            credit = Credit.objects.get(payment=instance)

            # Create a CreditRepayment record
            CreditRepayment.objects.create(
                credit=credit,
                payment=instance,
            )
            print(f"CreditRepayment created for Credit {credit.id}")

        except Credit.DoesNotExist:
            print(f"No Credit found for Payment {instance.payment_reference}")
            pass
