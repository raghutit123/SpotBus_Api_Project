from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import SchoolViewSet,RouteViewSet

router = routers.DefaultRouter()
router.register('school', SchoolViewSet)
router.register('route', RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
