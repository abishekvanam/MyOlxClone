from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView ,DestroyAPIView
from olx.models import *
from olx.serializers import *


class AdvtCreateApiView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        serializer.save(my_user=self.request.user)


class AdvtUpdateApiView(RetrieveUpdateAPIView):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_update(self, serializer):
        serializer.save(my_user=self.request.user)



class AdvtDeleteApiView(RetrieveDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

