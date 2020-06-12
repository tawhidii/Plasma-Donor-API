from rest_framework import serializers
from become_donors.models import BecomePlasmaDonors

class BecomePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BecomePlasmaDonors
        fields = '__all__'
        