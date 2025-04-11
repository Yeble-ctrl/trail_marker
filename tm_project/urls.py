from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Base Url for the accounts app
    path('trail-marker-accounts/', include('accounts.urls')),

    # Base Url for the user profile app
    path('profiles/', include('userProfile.urls')),

    # Urls for the simple jwt app
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
