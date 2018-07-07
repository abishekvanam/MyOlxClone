from django.shortcuts import get_object_or_404
from olx.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class SignUpAPi(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.data)
            return Response({'id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserPermissionsApi(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        """
            We will get here only if user is authenticated and is a staff member so simply return 200 status
            because a 403 status will be sent otherwise
        """

        return Response(status.HTTP_200_OK)




