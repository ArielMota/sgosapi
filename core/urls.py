
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),

    path('api//refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),

    path('api/', include('service_os.urls')),
]
