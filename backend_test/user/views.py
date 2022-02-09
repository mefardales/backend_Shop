from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def listUser(request):
    user = User.objects.all()
    serializer = UserSereializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Error creating user'}, status=400)
