from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserView, LoginView

app_name = "user"

urlpatterns = [
    path("register", UserView.as_view(), name="register"),
    path('login', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
