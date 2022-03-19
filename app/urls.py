from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
router=DefaultRouter()
router.register('getAddressDetails',AddressDetails,basename='AddressDetails')
urlpatterns = [
     path('api/',include(router.urls)),
]
