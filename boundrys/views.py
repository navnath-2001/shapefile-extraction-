from rest_framework import viewsets
from .disrtict import *
from .serializers import ind_adm2Serializer
from django.shortcuts import render
from .stateview import*
from rest_framework.views import APIView
# ViewSet for API CRUD operations on ind_adm2 model
class IndAdm2ViewSet(viewsets.ModelViewSet):
    queryset = ind_adm2.objects.all()
    serializer_class = ind_adm2Serializer


# Function-based view for rendering the homepage
def home_view(request):
    return render(request,"index.html")  # ✅ Corrected path slashes

class StateListView(APIView):
    def get(self, request):
        states = ind_adm1.objects.values('name_1').distinct()
        return Response(states)
