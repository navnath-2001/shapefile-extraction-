from rest_framework import generics
from .taluk import ind_adm3
from .serializers import IndAdm3Serializer
from .serializers import filter_district_by_state, retrune_boundry_by_district,DistrictSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .disrtict import ind_adm2
from .serializers import * #filter_district_by_state, retrune_boundry_by_district,DistrictSerializer,filter_taluk_by_district
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import json

# List all records
class IndAdm3ListView(generics.ListAPIView):
    queryset = ind_adm3.objects.all()
    serializer_class = IndAdm3Serializer

# Retrieve a single record by gid
class IndAdm3DetailView(generics.RetrieveAPIView):
    queryset = ind_adm3.objects.all()
    serializer_class = IndAdm3Serializer
    lookup_field = 'gid'
class DistrictListView(APIView):
    def get(self, request):
        districts = ind_adm2.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API View to return districts based on state


class TalukListByDistrict(APIView):
    @swagger_auto_schema(
        operation_summary="Get Taluks by District",
        operation_description="Send a taluk name (name_2),and get a list of districts in that state.",
        request_body=filter_taluk_by_district,
        responses={
            200: openapi.Response(
                description="List of Taluks",
                examples={
                    "application/json": {
                        "taluk": "Pune",
                        "taluks": ["Mulshi", "Haveli", "Shirur"]
                    }
                }
            ),
            400: "Bad Request - Invalid input"
        }
    )
    def post(self, request):
        serializer = filter_taluk_by_district(data=request.data)
        if serializer.is_valid():
            district_name = serializer.validated_data['name_2']
            taluks = ind_adm3.objects.filter(name_2=district_name).values_list('name_3', flat=True).distinct()

            return Response({
                "taluk": district_name,
                "taluks": list(taluks)
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class taluk_boundry(APIView):
    @swagger_auto_schema(
        operation_summary="Get boundary by taluk",
        operation_description="Provide a taluk name (`name_3`) and get its boundary geometry.",
        request_body=retrune_boundry_by_taluk,
        responses={
            200: openapi.Response(
                description="Taluk boundary geometry",
                examples={
                    "application/json": {
                        "taluk": "Mulshi",
                        "boundary": "MULTIPOLYGON (((...)))"
                    }
                }
            ),
            400: "Bad Request - Invalid input"
        }
    )
    def post(self, request):
        serializer = retrune_boundry_by_taluk(data=request.data)
        if serializer.is_valid():
            taluk_name = serializer.validated_data['name_3']  # ✅ correct field
            taluk = ind_adm3.objects.filter(name_3__iexact=taluk_name).first()

            if taluk:
                return Response({
                    "taluk": taluk.name_3,
                    "boundary": taluk.geom.geojson  # ✅ Only taluk geometry
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "Taluk not found"
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)