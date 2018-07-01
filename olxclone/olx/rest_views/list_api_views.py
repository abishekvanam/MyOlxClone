from rest_framework.generics import ListAPIView, RetrieveAPIView
from olx.models import *
from olx.serializers import *
from rest_framework.filters import SearchFilter,OrderingFilter
from olx.pagination import *
from django.db.models import Q

class AdvtListApiView(ListAPIView):
    #queryset = Advertisement.objects.all()

    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['title','description','category']
    #For searching the obtained results

    pagination_class = AdvtPageNumberPagination#AdvtLimitOffsetPagination#AdvtPageNumberPagination
    serializer_class = AdvertisementSerializer

    def get_queryset(self,*args,**kwargs):
        queryset_list = Advertisement.objects.all()
        search_text=self.request.GET.get("q")
        if search_text:
            queryset_list=queryset_list.filter(
                Q(title__icontains=search_text)|
                Q(category__icontains=search_text)|
                Q(description__icontains=search_text)
            )

        return queryset_list



class AdvtDetailApiView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pass




