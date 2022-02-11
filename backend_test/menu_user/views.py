from rest_framework.response import Response
from .models import MenuUser
from menu.models import Menu, MenuOptions
from .serializers import MenuUserSerializer
from rest_framework.decorators import api_view
from datetime import datetime
from commons.dateutils import time

@api_view(['GET'])
def getOrder(request, user_id):
    try:
        MenuUser.objects.get(id=user_id)
    except MenuUser.DoesNotExist:
        raise ValidationError({
            'Error this user is not valid'
        })
    today = time(0)
    if user_id == settings.ADMIN_ID:
        orders = MenuUser.objects.filter(order_date=today).all()
    else:
        orders = MenuUser.objects.filter(user=user_id, order_date=today).all()
    serializer = MenuUserSerializers(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createOrder(request, user_id):
    if time(1) > settings.CHECK_TIME:
        return Response({'Your request must be before 11:00 AM'},
                       status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        try:
            serilizer = MenuUserSerializer(order.data)
            user = MenuUser.objects.get(user=user_id)
        except MenuUser.DoesNotExist:
            raise ValidationError({'Error user does not exist'})

        try:
            if 'menu' not in request.data:
                raise ValidationError({'Error menu cannot be empty'})
            Menu.objects.get(id=order_data['menu'])
        except Menu.DoesNotExist:
            raise ValidationError({'Error menu is not valid'})

        try:
            menuOption = MenuOptions.objects.get(
                menu_id=request.data['menu'],
                option=request.data['menu_option'])
        except MenuOptions.DoesNotExist:
            raise ValidationError({
                'Error the menu is not valid'
            })
        if serializer.is_valid():
            order = UserMenu.objects.create(
                user=user,
                menu_option=menu_option,
                quantity=request.data['quantity'],
                especification=request.data['especification']
            )

            if 'order_date' in request.data:
                order.order_date.add(request.date['order_date'])

            return Response(serializer, status=status.HTTP_200_OK)
        return Response(
            serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
