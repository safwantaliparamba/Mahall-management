from django.urls import path 
from api.v1.customers import views


app_name = 'api_v1_customers'

urlpatterns = [
    path('',views.get_customers),
    path('create/',views.create_customer)
]