from django.urls import path 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.v1.users import views


app_name = "api_v1_users"

urlpatterns = [
    path('login/',views.admin_login),
    path('create-admin/',views.create_admin),
    path('reset-password/',views.reset_password),

    # jwt api's 
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]