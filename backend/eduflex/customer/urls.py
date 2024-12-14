from django.urls import path

from . import views

urlpatterns = [
    path("parent/onboarding/", views.ParentOnboardingView.as_view(), name="onboarding"),
]
