from django.conf import settings
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Menu
from .models import MenuOptions
from .serializers import MenuSerializer
from .serializers import MenuOptionsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from .task import send_slack

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
        send_slack(request.data['options'])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error creating the Menu'}, 
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#create menu options
@api_view(['POST'])
def createMenuOptions(request, user_id):
    if user_id != settings.ADMIN_ID:
        raise ValidationError(
            {'Error the user must be admin'}
        )
    try:
        Menu.objects.get(id=request.data['menu'])
    except Menu.DoesNotExist:
        return Response({'The menu does not exist'},
                           status=status.HTTP_404_NOT_FOUND)
            
    serializer = MenuOptionsSerializer(data=request.data)
    
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error creating the Menu Options'}, 
                       status=status.HTTP_400_BAD_REQUEST)

#update menu options
@api_view(['PUT'])
def updateMenuOptions(request, user_id):
    if user_id != settings.ADMIN_ID:
        menuOption = MenuOptions.objects.get(id=user_id)
        serializer = MenuOptionsSerializer(instance=menuOption, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error updating the Menu'}, 
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Error updating the menu options must be admin'},
                       status=status.HTTP_400_BAD_REQUEST)

#FIXME
#get menu
@api_view(['GET'])
def getMenu(request, uuid):
    try:
        menu = Menu.objects.get(uuid=uuid)
    except Menu.DoesNotExist:
        return Response({'Menu does not exist'}, 
                        status=status.HTTP_404_NOT_FOUND)

    menu_options = MenuOptions.objects.filter(menu=menu.id).all().order_by('option')
    serializer = MenuOptionsSerializer(menu_options, many=True)
    return Response({
        'id':menu.id,
        'uuid':menu.uuid,
        'date_menu':menu.date_menu,
        'options':serializer.data
    })
