from django.urls import path

from . import views

urlpatterns = [
    path("credit/", views.CreditView.as_view(), name="credit"),
    path(
        "credit_repayment/",
        views.CreditRepaymentView.as_view(),
        name="credit_repayment",
    ),
    path(
        "payment_schedule/",
        views.PaymentScheduleView.as_view(),
        name="payment_schedule",
    ),
    path(
        "parent/<int:parent_id>/credits/",
        views.CreditView.as_view(),
        name="parent_credits",
    ),
    path(
        "credit/<int:credit_id>/repayments/",
        views.CreditRepaymentView.as_view(),
        name="credit_repayments",
    ),
    path(
        "credit/<int:credit_id>/payment_schedule/",
        views.PaymentScheduleView.as_view(),
        name="credit_payment_schedule",
    ),
    path(
        "credit/initiate_payment/",
        views.CreditPaymentInitiationView.as_view(),
        name="initiate_credit_payment",
    ),
    path(
        "credit/verify_payment/",
        views.PaymentVerificationPollingView.as_view(),
        name="verify_credit_payment",
    ),
]
