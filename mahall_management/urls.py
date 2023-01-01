from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace='web')),

    path('api/v1/users/', include('api.v1.users.urls',namespace='api_v1_users')),
    path('api/v1/customers/', include('api.v1.customers.urls',namespace='api_v1_customers')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)