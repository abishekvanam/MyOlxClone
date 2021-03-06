from django.urls import path
from .views import *
from.rest_views import *

app_name='olx'

urlpatterns = [

    path('test/',test,name='test'),

    path('sample/',sample,name='sample'),

    #React
    #***********************************************************************************

    path('signup', SignUpAPi.as_view(), name="sign_up"),

    path('user_permissions', UserPermissionsApi.as_view(), name="user_permissions"),

    #Home
    # ***********************************************************************************

    path('',home,name='home'),

    #Auth
    #************************************************************************************


    path('signup/', SignUpView.as_view(), name='signup'),

    path('login/', LoginView.as_view(), name='login'),

    path('logout/', logout_user, name='logout'),

    #Advt
    #***********************************************************************************




    path('advt_list/',AdvtListView.as_view(),name='advt_list_view'),

    path('advt_list/<int:pk>/',AdvtDetailView.as_view(),name='advt_detail_view'),

    path('create_advt/',CreateAdvertisementView.as_view(),name='create_advt'),

    path('search_advt/',search_advt,name='search_advt'),


    path('like_advt/<int:advt_id>/',like_advt,name='like'),

    #Chat
    #***********************************************************************

    path('start_chat/<int:advt_id>/',start_chat,name='start_chat'),

    path('chat_list/',ChatListView.as_view(),name='chat_list'),

    path('chat_list/<int:chat_id>/',chat_detail_view,name='chat_detail_view'),


    #APIs
    #***********************************************************************************

    #Advt API
    #***********************************************************************************

    path('api/advt_list/',AdvtListApiView.as_view(),name='api_advt_list_view'),

    path('api/advt_list/<int:pk>/',AdvtDetailApiView.as_view(),name='api_advt_detail_view'),

    path('api/create_advt/',AdvtCreateApiView.as_view(),name='api_create_advt_view'),


    path('api/update_advt/<int:pk>/',AdvtUpdateApiView.as_view(),name='api_update_advt_view'),


    path('api/delete_advt/<int:pk>/',AdvtDeleteApiView.as_view(),name='api_delete_advt_view'),


    #Chats API
    #***********************************************************************************

    path('api/chat_list/',AllChatListApiView.as_view(),name='api_all_chat_list'),


    path('api/advt_list/<int:pk>/chat_list/',ChatListApiView.as_view(),name='api_chat_list'),

    path('api/chat_list/<int:pk>/',ChatDetailApiView.as_view(),name='api_chat_detail'),

]

