from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Service
from django.db import IntegrityError

class ListServices(APIView):
    def get(self, request):
        services = Service.objects.all()
        data = [{'name': s.name, 'url': s.url, 'service_type': s.service_type, 'api_location': s.api_location} for s in
                services]
        return Response({'status': 'success', 'data': data}, status=status.HTTP_200_OK)


class AddService(APIView):
    def post(self, request):
        data = request.data
        try:
            print(request)
            # Create a new device
            device = Service.objects.create(
                url=data.get('url'),
                name=data.get('name'),
                service_type=data.get('service_type'),
                api_location=data.get('api_location')
            )

            return Response({"status": "success", "message": "Service added successfully."})
        except IntegrityError as e:
            # Check if the error message is about the 'url' UNIQUE constraint
            if 'UNIQUE constraint failed: service_monitor_service.url' in str(e):
                return Response({"status": "error", "message": "This URL already exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": "error", "message": "An error occurred while adding the service."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
