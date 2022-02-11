from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def listUser(request, id):
    try:
        user = User.get(id=id)
    except User.DoesNotExist:
        return Response({'Error user does not exist'},status=status.HTTP_404_NOT_FOUND)
    user = User.objects.all()
    serializer = UserSereializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error creating user'}, status=HTTP_400_BAD_REQUEST)
