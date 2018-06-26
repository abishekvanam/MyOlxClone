from django.urls import path
from .views import *


app_name='olx'

urlpatterns = [

    path('test/',test,name='test'),

    path('sample/',sample,name='sample'),

    #Auth
    #***********************************************************************************


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

    path('chat_list/<int:chat_id>/',chat_detail_view,name='chat_detail_view')

]


