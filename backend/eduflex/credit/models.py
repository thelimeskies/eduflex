import uuid
from datetime import timedelta, date
from django.db import models
from django.utils.translation import gettext_lazy as _
from customer.models import Parents, Student
from school.models import School, SchoolFee
from ecraspay_django import models as ecraspay_models


# Credit Status Choices
class CreditStatus(models.TextChoices):
    PENDING = "PENDING", _("Pending")
    APPROVED = "APPROVED", _("Approved")
    DECLINED = "DECLINED", _("Declined")
    REJECTED = "REJECTED", _("Rejected")
    REPAYMENT = "REPAYMENT", _("Repayment")
    COMPLETED = "COMPLETED", _("Completed")
    OVERDUE = "OVERDUE", _("Overdue")


# Credit Model
class Credit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(
        Parents, on_delete=models.CASCADE, related_name="credits"
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="credits"
    )
    child = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="child_credits"
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="credits")
    terms = models.ManyToManyField(SchoolFee, related_name="credits")
    status = models.CharField(
        max_length=50, choices=CreditStatus.choices, default=CreditStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Credit")
        verbose_name_plural = _("Credits")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Credit for {self.parent.user.first_name} {self.parent.user.last_name}"

    @property
    def total_amount(self):
        """Calculate the total amount for the selected terms."""
        return self.terms.aggregate(total=models.Sum("amount"))["total"] or 0

    @property
    def total_repayment_amount(self):
        """Calculate total repayment amount with a 3% interest."""
        return round(self.total_amount * 1.03, 2)

    @property
    def is_active(self):
        """Check if the credit is active (approved and not fully repaid)."""
        return self.status == CreditStatus.APPROVED


# Credit Repayment Model
class CreditRepayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit = models.ForeignKey(
        Credit, on_delete=models.CASCADE, related_name="repayments"
    )
    payment = models.OneToOneField(
        ecraspay_models.Payment,
        on_delete=models.CASCADE,
        related_name="credit_repayment",
        help_text=_("The payment record from Ecraspay."),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Credit Repayment")
        verbose_name_plural = _("Credit Repayments")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Repayment for {self.credit} - {self.payment.payment_reference}"

    @property
    def amount_paid(self):
        """Return the amount paid from the linked Payment model."""
        return self.payment.amount

    @property
    def payment_status(self):
        """Return the current status of the payment."""
        return self.payment.status


# Payment Schedule Model
class PaymentSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit = models.ForeignKey(
        Credit, on_delete=models.CASCADE, related_name="schedules"
    )
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=CreditStatus.choices, default=CreditStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Payment Schedule")
        verbose_name_plural = _("Payment Schedules")
        ordering = ["due_date"]

    def __str__(self):
        return f"Installment for Credit {self.credit.id} - Due: {self.due_date}"

    def mark_completed(self):
        """Mark the payment schedule as completed."""
        self.status = CreditStatus.COMPLETED
        self.save()

    @property
    def is_overdue(self):
        """Check if the payment schedule is overdue."""
        return self.status == CreditStatus.PENDING and self.due_date < date.today()
