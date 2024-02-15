from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from api.views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='tokenobtainpairview'),
    path('token/refresh/',  TokenRefreshView.as_view(), name='tokenrefreshview'),
    path('register/', RegisterView.as_view(), name='registerview'),
    path('protected/', ProtectedView, name='protected')
]
