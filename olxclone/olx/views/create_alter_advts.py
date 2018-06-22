from django.views.generic import ListView,CreateView
from olx.models import *
from django.shortcuts import get_object_or_404,render,redirect
from olx.forms import *
from django.urls import reverse_lazy
import datetime
from django.http import HttpResponse


def test(request):
    return render(request,'olx/test.html',{})


class CreateAdvertisementView(CreateView):

    model = Advertisement
    form_class = AdvertisementForm
    success_url = reverse_lazy('olx:sample')
    template_name = 'olx/add_advt.html'

    # Need not send the form explicitly

    def post(self, request, *args, **kwargs):

        advt_form = AdvertisementForm(request.POST or None,request.FILES or None)

        my_user = request.user

        # import ipdb
        # ipdb.set_trace()

        if advt_form.is_valid():
            advt = advt_form.save(commit=False)

            advt.my_user = my_user

            advt.save()

        else:
            return HttpResponse("Enter valid details!!!")
        return redirect('olx:sample')

        pass





