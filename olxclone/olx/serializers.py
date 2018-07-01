from rest_framework import serializers
from olx.models import *
from rest_framework.serializers import HyperlinkedIdentityField,SerializerMethodField


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

    my_user=SerializerMethodField()
    image=SerializerMethodField()
    #Used to specify what attributes of an object
    #to be serialized using the function below.
    #Can be used for any objects mentioned below

    class Meta:
        model=Advertisement
        fields=(
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
            'my_user')


    def get_my_user(self,obj):
        return obj.my_user.username
    def get_image(self,obj):
        return obj.image.url





class ChatSerializer(serializers.ModelSerializer):

    receiver=SerializerMethodField()

    class Meta:
        model=ChatBox
        fields=(
            'sender',
            'receiver',
            'advt'
        )

    def get_receiver(self,obj):
        return obj.receiver.username
