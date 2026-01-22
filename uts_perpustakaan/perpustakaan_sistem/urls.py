from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('data.urls')), 
    
    path('api/', include('data.api_urls')), 

    path('api/login/', views.obtain_auth_token),
]