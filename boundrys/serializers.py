from rest_framework import serializers
from .disrtict import ind_adm2
from .state import ind_adm1

from .taluk import ind_adm3

class ind_adm2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ind_adm2
        fields = '__all__'
       


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ind_adm2
       


class IndAdm2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ind_adm1
        fields = '__all__'
      
        

class IndAdm3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ind_adm3
        fields = '__all__'
   
class filter_district_by_state(serializers.Serializer):
    name_1 = serializers.CharField()

class retrune_boundry_by_district(serializers.Serializer):
    name_2 = serializers.CharField(help_text="Name of the district")

class filter_taluk_by_district(serializers.Serializer):
    name_2 = serializers.CharField(help_text="Name of the district")

class retrune_boundry_by_taluk(serializers.Serializer):
    name_3 = serializers.CharField(help_text="Name of the district")

class return_boundry_by_state(serializers.Serializer):
    name_1 = serializers.CharField(help_text="State name")

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ind_adm1
        fields = ['name_1']