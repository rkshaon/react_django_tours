from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tours_api.models import Tour
from tours_api.serializers import TourSerializer

@api_view(['GET'])
def tourList(request):
    tours = Tour.objects.all().order_by('-id')
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)
