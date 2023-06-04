
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,  
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.user.api.urls'), name='users CRUD'),
    path('api/v1/', include('apps.file_explorer.api.urls'), name='Files API'),
    
    # Login and refresh token
    path('api/v1/login/', TokenObtainPairView.as_view(), name='Obtain Token'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='Refresh Token')
]
