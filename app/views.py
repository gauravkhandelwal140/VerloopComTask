from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
import requests
import json
from rest_framework_xml.renderers import XMLRenderer
from .serializers import *


class AddressDetails(viewsets.ViewSet):
    def create(self,request):
      serializer=AddressSerializer(data=request.data)
      apikey='Add API KEY Here'
      if serializer.is_valid():
        address=serializer.validated_data.get('address','')
        output_format=serializer.validated_data.get('output_format','')
        url='https://maps.googleapis.com/maps/api/geocode/json'
        params = {'address': address, 'key': apikey}
        x = requests.post(url, params=params)
        jsondata = json.loads(x.text)
        finaldata = {}
        if jsondata['status'] == 'OK':
          finaldata['coordinates'] = jsondata['results'][0]['geometry']['location']
          finaldata['address'] = jsondata['results'][0]['formatted_address']
          if output_format == 'json':
            return Response(finaldata,status=200)
          elif output_format == 'xml':
            x=XMLRenderer()
            x=x.render(data=finaldata)
            return HttpResponse(x, content_type='text/xml',status=200)
          else :
            return Response({'error':'invalid output_format'},status=400)
        else:
          return Response(jsondata, status=400)
      else:
        return Response({'error':serializer.errors},status=400)

