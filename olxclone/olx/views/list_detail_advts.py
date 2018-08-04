from django.shortcuts import get_object_or_404,render,redirect
from olx.models import *
from django.db.models import Q
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'olx/home.html',{})



class AdvtListView(ListView):

    model=Advertisement
    template_name = 'olx/advts_list.html'
    context_object_name = 'advt_list'

    def get_context_data(self, **kwargs):
        context = super(AdvtListView, self).get_context_data(**kwargs)

        context.update({'user_permissions': self.request.user.get_all_permissions})


        return context


class AdvtDetailView(DetailView):

    model=Advertisement
    template_name = 'olx/advt_detail.html'
    #context_object_name = 'advt_detail'

    def get_object(self, queryset=None):
        return get_object_or_404(Advertisement,**self.kwargs)

    def get_context_data(self, **kwargs):

        context = super(AdvtDetailView, self).get_context_data(**kwargs)

        advt=context.get('advertisement')



        context.update(
            {'advt':advt}
        )

        return context




def search_advt(request):

    search_text=request.GET['search_box']

    advt_list=Advertisement.objects.filter(Q(title__icontains=search_text)| Q(category__icontains=search_text)| Q(description__icontains=search_text))

    return render(request,'olx/advts_list.html',{'advt_list':advt_list})

@login_required(login_url="olx:login")
def like_advt(request,advt_id):


    a=Advertisement.objects.get(id=advt_id)



    a.interested_count+=1

    a.save()

    return redirect('olx:advt_detail_view',advt_id)

    pass


# class SearchAdvertisementView(ListView):
#     model = Advertisement
#     template_name = 'olx/advts_list.html'
#     context_object_name = 'advt_list'
#
#
#     def post(self, request, *args, **kwargs):
#
#
#
#     def get_context_data(self, **kwargs):
#         context = super(AdvtListView, self).get_context_data(**kwargs)
#
#
#         context.update(
#             {'advt_list':Advertisement.objects.filter}
#         )

