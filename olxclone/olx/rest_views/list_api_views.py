from rest_framework.generics import ListAPIView, RetrieveAPIView
from olx.models import *
from olx.serializers import *
from rest_framework.filters import SearchFilter,OrderingFilter


class AdvtListApiView(ListAPIView):
    queryset = Advertisement.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['title','description','category']
    
    serializer_class = AdvertisementSerializer


class AdvtDetailApiView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pass




