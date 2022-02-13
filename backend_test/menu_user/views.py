from rest_framework.response import Response
from django.conf import settings
from .models import MenuUser
from menu.models import Menu, MenuOptions
from .serializers import MenuUserSerializer
from rest_framework.decorators import api_view
from datetime import datetime
from commons.dateutils import time
from rest_framework.exceptions import ValidationError
from user.models import User
from rest_framework import status
from rest_framework.viewsets import ViewSet


class UserMenuAPIView(ViewSet):

    @api_view(['GET'])
    def getOrder(request, user_id):
        '''
        Get order from user
        '''
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'Error this user is not valid'},
                            status=status.HTTP_400_BAD_REQUEST 
                           )
        today = time(0)
        if user_id == settings.ADMIN_ID:
            orders = MenuUser.objects.filter(order_date=today).all()
        else:
            orders = MenuUser.objects.filter(user=user_id, order_date=today).all()
        serializer = MenuUserSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #FIXME
    @api_view(['POST'])
    def createOrder(request, user_id):
        '''
        Create order by admin
        '''
        if int(time(1)) > settings.CHECK_TIME:
            return Response({'Your request must be before 11:00 AM'},
                           status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            serializer = MenuUserSerializer(data=request.data)
            user = User.objects.get(id=user_id)
        except MenuUser.DoesNotExist:
            raise ValidationError({'Error user does not exist'})

        try:
            if 'menu' not in request.data:
                raise ValidationError({'Error menu cannot be empty'})
            Menu.objects.get(id=request.data['menu'])
        except Menu.DoesNotExist:
            raise ValidationError({'Error menu is not valid'})

        try:
            menu_option = MenuOptions.objects.filter(
                menu_id=request.data['menu'],
                option=request.data['menu_option']).all()[1]
        except MenuOptions.DoesNotExist:
            raise ValidationError({
                'Error the menu option is not valid'
            })

        if serializer.is_valid():
            order = MenuUser.objects.create(
                user=user,
                menu_option=menu_option,
                quantity=request.data['quantity'],
                specification=request.data['specification']
            )

            if 'order_date' in request.data:
                order.order_date.add(request.date['order_date'])

            return Response(
                {'message': 'Order create successfully',
                 'order': order.menu_option.description,
                 'specification':order.specification,
                 'order_date':order.order_date}, status=status.HTTP_200_OK)
        return Response(
            serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
