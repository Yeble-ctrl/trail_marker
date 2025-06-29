from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Base Url for the accounts app
    path('trail-marker-accounts/', include('accounts.urls')),

    # Base Url for the user profile app
    path('profiles/', include('userProfile.urls')),

    # Base URl for the blog app
    path('blogs/', include('blog.urls')),

    # Urls for the simple jwt app
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
