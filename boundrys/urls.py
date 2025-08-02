from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .districtview import DistrictListView , DistrictListByState,  District_boundry
from .stateview import *

from .talukview import *#IndAdm3ListView, IndAdm3DetailView,  TalukListByDistrict
from . import views
from .views import *

from .download import *
router = DefaultRouter()
router.register(r'ind-adm2', IndAdm2ViewSet, basename='ind-adm2')

urlpatterns = [
    # path('', include(router.urls)),
    path('api/districts/', DistrictListView.as_view(), name='district-list'),
    path('state/', IndAdm2ListView.as_view(), name='districts-list'),
    path('page/',home_view, name='home'),
    path('api/districts/', IndAdm2ListView.as_view(), name='districts-api'),
    path('taluk/', IndAdm3ListView.as_view(), name='indadm3-list'),
    # path('', homepage),
    path('filter_district_by_state/', DistrictListByState.as_view(),name= 'filter_district_by_state'),
    path(' District_boundry/',District_boundry.as_view(),name= ' District_boundry'),
    path(' filter_taluk_by_district/',TalukListByDistrict.as_view(),name= ' filter_taluk_by_district'),
    path('taluk_boundry/',taluk_boundry.as_view(),name= ' taluk_boundry'),
    path('download_taluk/', DownloadTalukGeoJSON.as_view(), name='download_taluk'),
    path('download/district/', DownloadDistrictGeoJSON.as_view(), name='download_district'),
    path('download/state/', DownloadStateGeoJSON.as_view(), name='download_state'),
    path('api/states/', StateListView.as_view(), name='state-list'),
]


    




