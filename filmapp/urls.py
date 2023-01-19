from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("kinolar", KinoModelViewSet)
router.register("aktyorlar", AktyorModelViewSet)
router.register("comments", CommentModelViewSet)


urlpatterns = [
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]