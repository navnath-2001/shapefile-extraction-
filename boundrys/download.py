import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .districtview import *
from .taluk import ind_adm3
from .serializers import *
from .stateview import *
class DownloadTalukGeoJSON(APIView):
    @swagger_auto_schema(
        operation_summary="Download taluk boundary as GeoJSON",
        operation_description="Provide taluk name (`name_3`) and download its geometry as GeoJSON file.",
        request_body=retrune_boundry_by_taluk,
        responses={
            200: openapi.Response(description="GeoJSON file download"),
            400: "Invalid input",
            404: "Not found"
        }
    )
    def post(self, request):
        serializer = retrune_boundry_by_taluk(data=request.data)
        if serializer.is_valid():
            taluk_name = serializer.validated_data['name_3']
            taluk = ind_adm3.objects.filter(name_3__iexact=taluk_name).first()
            
            if taluk:
                geojson_data = json.loads(taluk.geom.geojson)
                feature = {
                    "type": "Feature",
                    "geometry": geojson_data,
                    "properties": {
                        "name_3": taluk.name_3,
                        "name_2": taluk.name_2
                    }
                }

                feature_collection = {
                    "type": "FeatureCollection",
                    "features": [feature]
                }

                response = HttpResponse(
                    json.dumps(feature_collection),
                    content_type="application/geo+json"
                )
                response['Content-Disposition'] = f'attachment; filename={taluk.name_3}_boundary.geojson'
                return response
            
            return Response({"error": "Taluk not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#for the district download


class DownloadDistrictGeoJSON(APIView):
    @swagger_auto_schema(
        operation_summary="Download district boundary as GeoJSON",
        operation_description="Provide district name (`name_2`) to download boundary as GeoJSON.",
        request_body=retrune_boundry_by_district,
        responses={200: openapi.Response(description="GeoJSON")}
    )
    def post(self, request):
        serializer = retrune_boundry_by_district(data=request.data)
        if serializer.is_valid():
            name_2 = serializer.validated_data['name_2']
            district = ind_adm2.objects.filter(name_2__iexact=name_2).first()
            if district:
                geojson = {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": json.loads(district.geom.geojson),
                        "properties": {"name_2": district.name_2, "name_1": district.name_1}
                    }]
                }
                response = HttpResponse(json.dumps(geojson), content_type="application/geo+json")
                response['Content-Disposition'] = f'attachment; filename={district.name_2}_boundary.geojson'
                return response
            return Response({"error": "District not found"}, status=404)
        return Response(serializer.errors, status=400)


#for the state download
class DownloadStateGeoJSON(APIView):
    @swagger_auto_schema(
        operation_summary="Download state boundary as GeoJSON",
        operation_description="Provide state name (`name_1`) to download boundary as GeoJSON.",
        request_body=return_boundry_by_state,
        responses={200: openapi.Response(description="GeoJSON")}
    )
    def post(self, request):
        serializer = return_boundry_by_state(data=request.data)
        if serializer.is_valid():
            name_1 = serializer.validated_data['name_1']
            state = ind_adm1.objects.filter(name_1__iexact=name_1).first()
            if state:
                geojson = {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": json.loads(state.geom.geojson),
                        "properties": {"name_1": state.name_1}
                    }]
                }
                response = HttpResponse(json.dumps(geojson), content_type="application/geo+json")
                response['Content-Disposition'] = f'attachment; filename={state.name_1}_boundary.geojson'
                return response
            return Response({"error": "State not found"}, status=404)
        return Response(serializer.errors, status=400)
