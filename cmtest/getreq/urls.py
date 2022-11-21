from rest_framework.routers import DefaultRouter
from .views import GetreqViewSet
from django.urls import path, include


router = DefaultRouter('https://api.cmtelecom.com/texter/v1/support/operators')
router.register('getreq', GetreqViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
