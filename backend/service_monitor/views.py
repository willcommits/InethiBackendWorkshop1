from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Service

class ListServices(APIView):
    def get(self, request):
        services = Service.objects.all()
        data = [{'name': s.name} for s in services]
        return Response({'status': 'success', 'message': data}, status=status.HTTP_200_OK)
