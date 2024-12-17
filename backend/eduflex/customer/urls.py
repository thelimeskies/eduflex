from django.urls import path

from . import views

urlpatterns = [
    path("parent/onboarding/", views.ParentOnboardingView.as_view(), name="onboarding"),
    path(
        "parent/<int:parent_id>/children/",
        views.ChildrenView.as_view(),
        name="children",
    ),
    path(
        "parent/<int:parent_id>/credit_capacity_score/",
        views.ParentCreditAndCapacityScoreView.as_view(),
        name="credit_capacity_score",
    ),
]
