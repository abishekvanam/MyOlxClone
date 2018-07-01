from olx.models import ChatBox,Messages
from rest_framework.generics import ListAPIView, RetrieveAPIView
from olx.serializers import ChatListSerializer,ChatDetailSerializer


class AllChatListApiView(ListAPIView):
    queryset = ChatBox.objects.all()
    serializer_class = ChatListSerializer


class ChatListApiView(ListAPIView):#ListAPIView):
    #queryset = ChatBox.objects.all()
    serializer_class = ChatListSerializer

    # lookup_field = 'advt'
    # lookup_url_kwarg = 'pk'

    def get_queryset(self):
        advt_id=self.kwargs['pk']
        return ChatBox.objects.filter(advt=advt_id)


class ChatDetailApiView(RetrieveAPIView):
    queryset = ChatBox.objects.all()
    serializer_class = ChatDetailSerializer




