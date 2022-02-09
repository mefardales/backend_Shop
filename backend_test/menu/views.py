from rest_framework.response import Response
from .models import Menu
from .models import MenuOptions
from .serializers import MenuSerializer
from .serializers import MenuOptionsSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def createMenu(request):
    serializer = MenuSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Error creating the Menu'}, status=400)

@api_view(['POST'])
def createMenuOptions(request):
    serializer = MenuOptionsSerializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Error creating the Menu Options'}, status=400)

@api_view(['POST'])
def updateMenuOptions(request, pk):
    menuOption = MenuOptions.objects.get(id=pk)
    serializer = MenuOptionsSerializers(instance=menuOption, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Error updating the Menu'}, status=400)
        
