from django.urls import path, re_path
from api.v1.customers import views


app_name = 'api_v1_customers'

urlpatterns = [
    re_path(r'^chief/customers/$',views.get_customers),
    re_path(r'^chief/create/$',views.create_customer),
    re_path(r'^chief/update/(?P<customer_id>.*)/$',views.update_customer)
]