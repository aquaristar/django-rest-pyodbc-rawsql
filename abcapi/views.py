from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from abcapi.serializers import *
from abcapi.models import *
from itertools import chain
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer




class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that save Da1YahooHeader, Da1YahooShipto, Da1YahooDetail objects in an order.
    """
    queryset = User.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post', 'head']

    def create(self, request):
        yahooh_data = request.data.pop('yahooh')
        if (yahooh_data):
            Da1YahooHeader.objects.create_yahooh(yahooh_data)
        #yahooh = Da1YahooHeaderSerializer(data=yahooh_data)
        # if yahooh.is_valid():
        #     yahooh.save()

        yahoos_data = request.data.pop('yahoos')
        if (yahoos_data):
            Da1YahooShipto.objects.create_yahoos(yahoos_data)
        # yahoos = Da1YahooShiptoSerializer(data=yahoos_data)
        # if yahoos.is_valid():
        #     yahoos.save()
        
        yahoods_data = request.data.pop('yahood')
        for yahood_data in yahoods_data:
            Da1YahooDetail.objects.create_yahood(yahood_data)
        #    yahood = Da1YahooDetailSerializer(data=yahood_data)
        #     if yahood.is_valid():
        #         yahood.save()
        
        return Response(request.data)




class DskGiftMainViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that retrieve Gift object.
    """
    queryset = DskGiftMain.objects.all()
    serializer_class = DskGiftMainSerializer

    def get_queryset(self):
        accountNum = self.request.query_params.get('accountNum', None)
        scratchNum = self.request.query_params.get('scratchNum', None)

        queryset = DskGiftMain.objects.get_gift(accountNum, scratchNum)

        return queryset



class Da7InventoryStoreViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that retrieve Inventory object.
    """
    queryset = Da7InventoryStore.objects.all()
    serializer_class = Da7InventoryStoreSerializer

    def get_queryset(self):
        productId = self.request.query_params.get('productId', None)

        queryset = Da7InventoryStore.objects.get_inventory(productId)
        
        return queryset