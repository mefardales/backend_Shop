from rest_framework.response import Response
from .models import Menu
from .models import MenuOptions
from .serializers import MenuSerializer
from .serializers import MenuOptionsSerializer
from rest_framework.decorators import api_view
from rest_framework import status

#list menu
@api_view(['GET'])
def listMenu(request):
    try:
        menu = Menu.objects.all()
    except Menu.DoesNotExist:
        return Response({'Error not exist the menu'}, status=status.HTTP_400_NOT_FOUND)
    serializer = MenuSerializer(menu, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#create menu
@api_view(['POST'])
def createMenu(request, user_id):
    if user_id != settings.ADMIN_ID:
        raise ValidationError(
            {'Error invalid user'}
        )
    serializer = MenuSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error creating the Menu'}, 
                        status=status.HTTP_422_UNPROCESSABLE_EKNTITY)

#create menu options
@api_view(['POST'])
def createMenuOptions(request, user_id):
    if user_id != settings.ADMIN_ID:
        raise ValidationError(
            {'Error the user must be admin'}
        )
    serializer = MenuOptionsSerializers(data=request.data)
    
    if serializer.is_valid():
        try:
            Menu.objects.get(id=request.data['menu'])
        except Menu.DoesNotExist:
            return Response({'The menu does not exist'},
                           status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error creating the Menu Options'}, 
                       status=status.HTTP_400_BAD_REQUEST)

#update menu options
@api_view(['PUT'])
def updateMenuOptions(request, user_id, pk):
    if user_id != settings.ADMIN_ID:
        menuOption = MenuOptions.objects.get(id=pk)
        serializer = MenuOptionsSerializers(instance=menuOption, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error updating the Menu'}, 
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Error updating the menu options must be admin'},
                       status=status.HTTP_400_BAD_REQUES)

#get menu
@api_view(['GET'])
def getMenu(request, uuid):
    try:
        menu = Menu.objects.get(uuid=uuid)
    except Menu.DoesNotExists:
        return Response({'Menu does not exist'}, 
                        status=status.HTTP_404_NOT_FOUND)
    menu_options = MenuOptions.objects.filter(
        menu=menu.id).all().order_by('option')
    serializer = MenuOptionsSerializer(menu_options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
