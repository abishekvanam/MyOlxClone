from olx.models import ChatBox,Messages
from rest_framework.generics import ListAPIView, RetrieveAPIView
from olx.serializers import ChatSerializer


class ChatListApiView(ListAPIView):
    queryset = ChatBox.objects.all()
    serializer_class = ChatSerializer

