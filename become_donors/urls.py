from django.urls import include,path
from rest_framework import routers
from become_donors.api_views import BecomeDonorViewSet
router = routers.DefaultRouter()
router.register(r'api',BecomeDonorViewSet)

urlpatterns = [
    path('',include(router.urls))
]

