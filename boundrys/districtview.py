from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .disrtict import ind_adm2

from .serializers import filter_district_by_state, retrune_boundry_by_district,DistrictSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import json

class DistrictListView(APIView):
    def get(self, request):
        districts = ind_adm2.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API View to return districts based on state
class DistrictListByState(APIView):
    @swagger_auto_schema(
        operation_summary="Get districts by state",
        operation_description="Provide a state name (`name_1`) and get a list of districts in that state.",
        request_body=filter_district_by_state,
        responses={
            200: openapi.Response(
                description="List of districts",
                examples={
                    "application/json": {
                        "state": "Maharashtra",
                        "districts": ["Pune", "Nagpur", "Mumbai"]
                    }
                }
            ),
            400: "Bad Request - Invalid input"
        }
    )
    def post(self, request):
        serializer =filter_district_by_state(data=request.data)
        if serializer.is_valid():
            state_name = serializer.validated_data['name_1']
            
            # Filter districts by state name
            districts = ind_adm2.objects.filter(name_1=state_name).values_list('name_2', flat=True).distinct()
            
            return Response({
                "state": state_name,
                "districts": list(districts)
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class District_boundry(APIView):
    @swagger_auto_schema(
        operation_summary="Get boundary by district",
        operation_description="Provide a district name (`name_2`) and get its boundary geometry.",
        request_body=retrune_boundry_by_district,
        responses={
            200: openapi.Response(
                description="District boundary geometry",
                examples={
                    "application/json": {
                        "district": "Ahmednagar",
                        "boundary": "MULTIPOLYGON (((...)))"
                    }
                }
            ),
            400: "Bad Request - Invalid input"
        }
    )
    def post(self, request):
        serializer = retrune_boundry_by_district(data=request.data)
        if serializer.is_valid():
            district_name = serializer.validated_data['name_2']
            district = ind_adm2.objects.filter(name_2=district_name).first()
            
            if district:
                return Response({
                    "district": district.name_2,
                    "boundary": district.geom.geojson  # Convert geometry to GeoJSON format
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "District not found"
                }, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
