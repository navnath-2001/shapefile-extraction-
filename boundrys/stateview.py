from rest_framework import generics
from .state import ind_adm1
from .serializers import IndAdm2Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .state import IndAdm1
from django.contrib.gis.db import models



class IndAdm2ListView(generics.ListAPIView):
    queryset = ind_adm1.objects.all()
    serializer_class = IndAdm2Serializer


@api_view(['GET'])
def get_districts_by_state(request):
    state_name = request.GET.get('state')
    if not state_name:
        return Response({"error": "State parameter is required"}, status=400)
    
    districtss = IndAdm1.objects.filter(name_1=state_name).values_list('name_2', flat=True).distinct()
    return Response([{"name": d} for d in districtss])
