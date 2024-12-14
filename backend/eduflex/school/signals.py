# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import School, SchoolClass, SchoolCategory


# @receiver(post_save, sender=School)
# def create_default_classes(sender, instance, created, **kwargs):
#     if created and instance.categories:
#         category_classes = {
#             "Primary": [f"Primary {i}" for i in range(1, 7)],
#             "Junior Secondary": [f"JSS {i}" for i in range(1, 4)],
#             "Senior Secondary": [f"SSS {i}" for i in range(1, 4)],
#         }

#         for category in instance.categories:
#             if category in category_classes:
#                 for class_name in category_classes[category]:
#                     SchoolClass.objects.get_or_create(
#                         school=instance,
#                         category=category,
#                         name=class_name,
#                     )
