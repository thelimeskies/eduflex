from django.urls import path

from . import views

urlpatterns = [
    path("onboarding/", views.SchoolOnboardingView.as_view(), name="onboarding"),
    path("fee/", views.SchoolFeeView.as_view(), name="fee"),
]
