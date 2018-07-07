from rest_framework import serializers
from olx.models import *
from rest_framework.serializers import HyperlinkedIdentityField,SerializerMethodField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')





class MessagesSerializer(serializers.ModelSerializer):

    sender=SerializerMethodField()

    class Meta:
        model=Messages
        fields=(
            'message_text',
            'message_time',
            'sender'
        )


    def get_sender(self,obj):
        return obj.sender.username

class ChatListSerializer(serializers.ModelSerializer):

    receiver=SerializerMethodField()

    messages_count=SerializerMethodField()

    detail_url = HyperlinkedIdentityField(
        view_name='olx:api_chat_detail'
    )

    class Meta:
        model=ChatBox
        fields=(
            'detail_url',
            'sender',
            'receiver',
            'advt',
            'messages_count'
        )

    def get_receiver(self,obj):
        return obj.receiver.username

    def get_messages_count(self,obj):
        return (Messages.objects.filter(chat_box__id=obj.id)).count()


class ChatDetailSerializer(serializers.ModelSerializer):

    receiver=SerializerMethodField()
    messages=SerializerMethodField()

    class Meta:
        model=ChatBox
        fields = (
            'sender',
            'receiver',
            'advt',
            'messages'
        )

    def get_receiver(self,obj):
        return obj.receiver.username

    def get_messages(self,obj):
        return MessagesSerializer(Messages.objects.filter(chat_box__id=obj.id),#sender__username=obj.sender),
                                  many=True).data


class AdvertisementSerializer(serializers.ModelSerializer):

    detail_url=HyperlinkedIdentityField(
        view_name='olx:api_advt_detail_view'
    )

    update_url=HyperlinkedIdentityField(
        view_name='olx:api_update_advt_view'
    )


    delete_url=HyperlinkedIdentityField(
        view_name='olx:api_delete_advt_view'
    )

    chat_list_url=HyperlinkedIdentityField(
        view_name='olx:api_chat_list'
    )

    my_user=SerializerMethodField()
    image=SerializerMethodField()
    chat_count=SerializerMethodField()


    #Used to specify what attributes of an object
    #to be serialized using the function below(below meta block).
    #Can be used for any objects mentioned below(in meta block).

    class Meta:
        model=Advertisement
        fields=(
            'id',
            'detail_url',
            'update_url',
            'delete_url',
            'title',
            'description',
            'category',
            'item_type',
            'price',
            'image',
            'posted_on',
            'interested_count',
            'my_user',
            'chat_list_url',
            'chat_count',
        )


    def get_my_user(self,obj):
        return obj.my_user.username

    def get_image(self,obj):
        return obj.image.url

    def get_chat_count(self,obj):
        return ChatBox.objects.filter(advt=obj.id).count()
        pass











