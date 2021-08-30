from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView



urlpatterns = [
    
    
    path("",views.apiconfig,name="apiconfig"),
    
    
    # login
    path('login/', TokenObtainPairView.as_view(), name='login_view'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/',RegisterView.as_view(),name="Register"),


]

