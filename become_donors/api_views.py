from rest_framework import viewsets
from become_donors.serializers import BecomePlasmaDonorSerializer
from become_donors.models import BecomePlasmaDonors

class BecomeDonorViewSet(viewsets.ModelViewSet):
    queryset = BecomePlasmaDonors.objects.all().order_by('name')
    serializer_class = BecomePlasmaDonorSerializer