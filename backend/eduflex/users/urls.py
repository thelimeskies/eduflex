from django.urls import path, include
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import (
    RegisterView,
    ResendEmailVerificationView,
    VerifyEmailView,
)
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView,
)
from django.urls import path, re_path


urlpatterns = [
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path(
        "verify-email/",
        VerifyEmailView.as_view(),
        name="rest_verify_email",
    ),
    path(
        "resend-email-verification/",
        ResendEmailVerificationView.as_view(),
        name="rest_resend_email_verification",
    ),
    path("refresh-token/", get_refresh_view().as_view(), name="token_refresh"),
]
