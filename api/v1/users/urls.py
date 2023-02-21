from django.urls import re_path,path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.v1.users import views


app_name = "api_v1_users"

urlpatterns = [
    ####----------chief-----------###### 
    re_path(r'^login/$',views.admin_login),
    re_path(r'^create-admin/$',views.create_admin),
    re_path(r'^reset-password/$',views.reset_password),
    # jwt authentication
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]