import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to="school/logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")
        ordering = ["name"]


class SchoolCategory(models.TextChoices):
    PRIMARY = "Primary", _("Primary")
    JUNIOR_SECONDARY = "Junior Secondary", _("Junior Secondary")
    SENIOR_SECONDARY = "Senior Secondary", _("Senior Secondary")


class SchoolClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classes")
    category = models.CharField(
        max_length=20, choices=SchoolCategory.choices, default=SchoolCategory.PRIMARY
    )
    name = models.CharField(max_length=50, help_text=_("E.g., Primary 1, JSS 1, SSS 1"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.school.name} - {self.name} ({self.category})"

    class Meta:
        verbose_name = _("School Class")
        verbose_name_plural = _("School Classes")
        ordering = ["school", "category", "name"]


class Term(models.TextChoices):
    FIRST_TERM = "First Term", _("First Term")
    SECOND_TERM = "Second Term", _("Second Term")
    THIRD_TERM = "Third Term", _("Third Term")


class SchoolFee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.CASCADE, related_name="fees"
    )
    term = models.CharField(max_length=15, choices=Term.choices)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text=_("Enter the fee amount per term")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.school_class} - {self.term} - ₦{self.amount}"

    class Meta:
        verbose_name = _("School Fee")
        verbose_name_plural = _("School Fees")
        ordering = ["school_class", "term"]
