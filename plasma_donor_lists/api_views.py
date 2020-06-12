from rest_framework import viewsets
from plasma_donor_lists.serializers import(
    A_PositivePlasmaDonorSerializer,
    A_NegativePlasmaDonorSerializer,
    B_PositivePlasmaDonorSerializer,
    B_NegativePlasmaDonorSerializer,
    AB_PositivePlasmaDonorSerializer,
    AB_NegativePlasmaDonorSerializer,
    O_PositivePlasmaDonorSerializer,
    O_NegativePlasmaDonorSerializer

) 
from plasma_donor_lists.models import(
    A_PositiveDonorList,
    A_NegativeDonorList,
    B_PositiveDonorList,
    B_NegativeDonorList,
    AB_PositiveDonorList,
    AB_NegativeDonorList,
    O_PositiveDonorList,
    O_NegativeDonorList
)
class A_PositivePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = A_PositiveDonorList.objects.all().order_by('name')
    serializer_class = A_PositivePlasmaDonorSerializer


class A_NegativePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = A_NegativeDonorList.objects.all().order_by('name')
    serializer_class = A_NegativePlasmaDonorSerializer


class B_PositivePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = B_PositiveDonorList.objects.all().order_by('name')
    serializer_class = B_PositivePlasmaDonorSerializer


class B_NegativePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = B_NegativeDonorList.objects.all().order_by('name')
    serializer_class = B_NegativePlasmaDonorSerializer


class AB_PositivePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = AB_PositiveDonorList.objects.all().order_by('name')
    serializer_class = AB_PositivePlasmaDonorSerializer

class AB_NegativePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = AB_NegativeDonorList.objects.all().order_by('name')
    serializer_class = AB_NegativePlasmaDonorSerializer


class O_PositivePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = O_PositiveDonorList.objects.all().order_by('name')
    serializer_class = O_PositivePlasmaDonorSerializer


class O_NegativePlasmaDonorViewSet(viewsets.ModelViewSet):
    queryset = O_NegativeDonorList.objects.all().order_by('name')
    serializer_class = O_NegativePlasmaDonorSerializer