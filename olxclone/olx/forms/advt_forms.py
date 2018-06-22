from django import forms
from olx.models import *


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model=Advertisement
        exclude=['id','posted_on','interested_count','my_user']


        widgets={

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),

            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

            #'category':forms.Input(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

            'item_type':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

            'price':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

            #'image':forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

        }

    pass

