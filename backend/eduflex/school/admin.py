from django.contrib import admin

from .models import School, SchoolFee, SchoolClass


class SchoolFeeInline(admin.TabularInline):
    model = SchoolFee
    extra = 1


class SchoolClassInline(admin.TabularInline):
    model = SchoolClass
    extra = 1
    show_change_link = True  # Allow linking to the SchoolClass admin for editing


class NestedSchoolFeeInline(admin.StackedInline):
    model = SchoolFee
    extra = 1
    fields = ["school_class", "fee_amount", "description"]  # Adjust fields as necessary


class SchoolClassInlineWithFees(admin.StackedInline):
    model = SchoolClass
    extra = 1
    show_change_link = True
    inlines = [SchoolFeeInline]  # Include SchoolFee inline for nested display


class SchoolAdmin(admin.ModelAdmin):
    inlines = [SchoolClassInline]
    fields = (
        "name",
        "address",
        "phone",
        "email",
        "website",
        "logo",
        "admin",
    )

    ordering = ["name"]

    list_display = [
        "name",
        "address",
        "phone",
        "email",
        "website",
        "admin",
    ]

    search_fields = [
        "name",
        "address",
        "phone",
        "email",
    ]

    list_filter = [
        "admin",
    ]


class SchoolClassAdmin(admin.ModelAdmin):
    inlines = [SchoolFeeInline]

    fields = (
        "school",
        "category",
        "name",
    )

    ordering = ["school", "category", "name"]

    list_display = [
        "school",
        "category",
        "name",
    ]

    search_fields = [
        "school__name",
        "category",
        "name",
    ]

    list_filter = [
        "category",
    ]


admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
