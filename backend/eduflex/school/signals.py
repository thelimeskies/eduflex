from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import School, SchoolClass, SchoolCategory



Providing a complete codebase with all the necessary files, models, serializers, views, URLs, and configuration is a larger task. Below, I’ve structured the entire backend application based on your requirements. This includes all the files you’d need in a Django project to handle school onboarding, class creation, and fee management.

Project Structure
markdown
Copy code
school_management/
├── manage.py
├── school_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── schools/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
1. models.py
python
Copy code
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class SchoolCategory(models.TextChoices):
    PRIMARY = "Primary", _("Primary")
    JUNIOR_SECONDARY = "Junior Secondary", _("Junior Secondary")
    SENIOR_SECONDARY = "Senior Secondary", _("Senior Secondary")


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to="school/logos/", blank=True, null=True)
    categories = models.JSONField(
        default=list,
        help_text=_("Select school categories (e.g., Primary, Junior Secondary)"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")
        ordering = ["name"]


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
2. signals.py
python
Copy code
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import School, SchoolClass, SchoolCategory


@receiver(post_save, sender=School)
def create_default_classes(sender, instance, created, **kwargs):
    if created and instance.categories:
        category_classes = {
            "Primary": [f"Primary {i}" for i in range(1, 7)],
            "Junior Secondary": [f"JSS {i}" for i in range(1, 4)],
            "Senior Secondary": [f"SSS {i}" for i in range(1, 4)],
        }

        for category in instance.categories:
            if category in category_classes:
                for class_name in category_classes[category]:
                    SchoolClass.objects.get_or_create(
                        school=instance,
                        category=category,
                        name=class_name,
                    )