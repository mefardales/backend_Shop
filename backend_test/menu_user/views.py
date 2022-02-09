from rest_framework.response import Response
from .models import MenuUser
from .serializers import MenuUserSerializer
from rest_framework.decorators import api_view
from datetime import datetime
from commons.dateutils import time

@api_view(['GET'])
def listMenuUser(request):
    menuUser = MenuUser.objects.all()
    serializer = ManueUserSerializer(event, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createMenuUser(request):
    if time(1) > settings.CHECK_TIME:
        return Response({'Your request must be before 11:00 AM'},status=400)
    else:
        serializer = MenuUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)




