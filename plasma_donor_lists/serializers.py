from rest_framework import serializers
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
class A_PositivePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = A_PositiveDonorList
        fields = '__all__'



class A_NegativePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = A_NegativeDonorList
        fields = '__all__'



class B_PositivePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = B_PositiveDonorList
        fields = '__all__'
        

class B_NegativePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = B_NegativeDonorList
        fields = '__all__'


class AB_PositivePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AB_PositiveDonorList
        fields = '__all__'


class AB_NegativePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AB_NegativeDonorList
        fields = '__all__'


class O_PositivePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = O_PositiveDonorList
        fields = '__all__'

class O_NegativePlasmaDonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = O_NegativeDonorList
        fields = '__all__'