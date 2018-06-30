from rest_framework import serializers
from olx.models import *
from rest_framework.serializers import HyperlinkedIdentityField


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





