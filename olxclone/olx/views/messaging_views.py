from django.shortcuts import get_object_or_404,render,redirect
from olx.models import *
from django.db.models import Q
from django.views.generic import ListView,DetailView

def start_chat(request,advt_id):

    if request.method=='POST':

        chat_message=request.POST['chat_message']

        advt_obj=Advertisement.objects.get(id=advt_id)

        if ChatBox.objects.exists() and (ChatBox.objects.filter(Q(sender=request.user.username)&Q(receiver=advt_obj.my_user)).exists() or ChatBox.objects.filter((Q(receiver=request.user)&Q(sender=advt_obj.my_user.username))).exists()):


            chat_obj=ChatBox.objects.get(Q(Q(sender=request.user.username)&Q(receiver=advt_obj.my_user))|Q(Q(receiver=request.user)&Q(sender=advt_obj.my_user.username)))



            chat_box_obj=chat_obj


        else:

            # advt_obj = Advertisement.objects.values('my_user','id').get(id=advt_id)

            chat_obj1 = ChatBox(sender=request.user.username,receiver=advt_obj.my_user, advt=advt_obj)

            chat_obj1.save()

            chat_box_obj = chat_obj1


        msg=Messages(message_text=chat_message,chat_box=chat_box_obj,sender=request.user)
        msg.save()

        return render(request,'olx/my_messages.html',
                      {
                        'my_messages':Messages.objects.filter(Q(chat_box__advt__id=advt_id)&
                                                              Q(sender=request.user)&
                                                              Q(chat_box__receiver=advt_obj.my_user)),

                        'advt_id':advt_id
                      })

    return render(request,'olx/my_messages.html',{'my_messages':[],'advt_id':advt_id})


class ChatListView(ListView):

    model=ChatBox

    template_name = 'olx/chat_list.html'

    def get_context_data(self, **kwargs):

        context=super(ChatListView,self).get_context_data(**kwargs)

        context.update({'user_permissions':self.request.user.get_all_permissions})

        my_chats=list(ChatBox.objects.filter(Q(receiver__id=self.request.user.id)|Q(sender=self.request.user.username)))
        # received_chats=ChatBox.objects.filter(messages__sender__id=self.request.user.id)

        # if received_chats.exists():
        #     r=[]
        #     r.append(received_chats[0])
        #     my_chats+=r

        # import ipdb
        # ipdb.set_trace()

        context.update(
            {'my_chats':my_chats}
        )

        return context




def chat_detail_view(request,chat_id):

    if request.method=='POST':
        chat_message = request.POST['chat_message']
        msg = Messages(message_text=chat_message, chat_box=ChatBox.objects.get(id=chat_id), sender=request.user)
        msg.save()

    msgs=Messages.objects.filter(chat_box__id=chat_id)

    return render(request,'olx/chat_detail.html',
                  {
                      'all_messages':msgs,
                      'chat_id':chat_id
                  })

    pass




