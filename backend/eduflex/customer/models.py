import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Parents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="parent")
    phone = models.CharField(max_length=15)
    address = models.TextField()
    occupation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Parent")
        verbose_name_plural = _("Parents")
        ordering = ["user__first_name", "user__last_name"]


class ParentIDCategory(models.TextChoices):
    NATIONAL_ID = "National ID", _("National ID")
    INTERNATIONAL_PASSPORT = "International Passport", _("International Passport")
    DRIVER_LICENSE = "Driver License", _("Driver License")
    VOTER_CARD = "Voter Card", _("Voter Card")


class ParentKYC(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.OneToOneField(Parents, on_delete=models.CASCADE, related_name="kyc")

    # Financial Information
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    employer = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    bank_account_statement = models.FileField(
        upload_to="parent/kyc/bank_account_statement/"
    )

    # Identity Information
    id_type = models.CharField(max_length=50, choices=ParentIDCategory.choices)
    id_number = models.CharField(max_length=50, unique=True, db_index=True)
    id_front = models.FileField(upload_to="parent/kyc/id_front/", blank=True, null=True)
    id_back = models.FileField(upload_to="parent/kyc/id_back/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.parent.user.first_name} {self.parent.user.last_name}"

    class Meta:
        verbose_name = _("Parent KYC")
        verbose_name_plural = _("Parent KYC")


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(
        Parents, on_delete=models.CASCADE, related_name="children"
    )
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="students"
    )
    school_class = models.ForeignKey(
        "school.SchoolClass", on_delete=models.CASCADE, related_name="student_class"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ["first_name", "last_name"]


class ParentCreditCapacityScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.OneToOneField(
        Parents, on_delete=models.CASCADE, related_name="credit_capacity_score"
    )
    credit_score = models.DecimalField(max_digits=5, decimal_places=2)
    capacity_score = models.DecimalField(max_digits=5, decimal_places=2)
    
    credit_score_description = models.CharField(max_length=50)
    capacity_score_description = models.CharField(max_length=50)

    credit_score_recommendation = models.TextField()
    capacity_score_recommendation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.parent.user.first_name} {self.parent.user.last_name}"

    class Meta:
        verbose_name = _("Parent Credit and Capacity Score")
        verbose_name_plural = _("Parent Credit and Capacity Scores")
        ordering = ["parent__user__first_name", "parent__user__last_name"]
