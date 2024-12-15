from django.contrib import admin

from .models import Parents, Student, ParentKYC


class ParentKYCInline(admin.StackedInline):
    model = ParentKYC
    extra = 1


class ParentsAdmin(admin.ModelAdmin):

    inlines = [ParentKYCInline]
    fields = (
        "user",
        "phone",
        "address",
        "occupation",
    )

    ordering = ["user__first_name", "user__last_name"]

    list_display = [
        "user",
        "phone",
        "address",
        "occupation",
    ]

    search_fields = [
        "user__first_name",
        "user__last_name",
        "phone",
    ]

    list_filter = [
        "occupation",
    ]


admin.site.register(Parents, ParentsAdmin)
