from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import MyTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('token-access/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
