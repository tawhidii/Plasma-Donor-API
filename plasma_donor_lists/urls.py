from django.urls import include, path
from rest_framework import routers
from plasma_donor_lists.api_views import(
    A_PositivePlasmaDonorViewSet,
    A_NegativePlasmaDonorViewSet,
    B_PositivePlasmaDonorViewSet,
    B_NegativePlasmaDonorViewSet,
    AB_PositivePlasmaDonorViewSet,
    AB_NegativePlasmaDonorViewSet,
    O_PositivePlasmaDonorViewSet,
    O_NegativePlasmaDonorViewSet

)
router = routers.DefaultRouter()
router.register(r'a-positive-donor',A_PositivePlasmaDonorViewSet)
router.register(r'a-negative-donor',A_NegativePlasmaDonorViewSet)
router.register(r'b-positive-donor',B_PositivePlasmaDonorViewSet)
router.register(r'b-negative-donor',B_NegativePlasmaDonorViewSet)
router.register(r'ab-positive-donor',AB_PositivePlasmaDonorViewSet)
router.register(r'ab-negative-donor',AB_NegativePlasmaDonorViewSet)
router.register(r'o-positive-donor',O_PositivePlasmaDonorViewSet)
router.register(r'o-negative-donor',O_NegativePlasmaDonorViewSet)



urlpatterns = [
    path('', include(router.urls)),
  
]