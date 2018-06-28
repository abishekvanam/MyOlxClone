from rest_framework.generics import ListAPIView, RetrieveAPIView
from olx.models import *
from olx.serializers import *


class AdvtListApiView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvtDetailApiView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pass




