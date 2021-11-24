from django import forms
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User
from market.models import MarketPostCategory, SellerMarketPost
from PIL import Image


# CREATE A "Datepicker" FEATURE TO INHERIT FROM DJANGO "forms.DateInput"
class Datepicker(forms.DateInput):
    input_type = 'datetime-local'




class SellerMarketPostForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'Title'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder':'Description'}))
    date_posted = forms.DateTimeField(label='Date', widget=Datepicker(attrs={'placeholder':'Date'}))
    telephone_number = forms.CharField(label='Telephone Number',widget=forms.NumberInput(attrs={'placeholder': 'Telephone Number'}))
    price = forms.CharField(label='Price', widget=forms.NumberInput(attrs={'placeholder':'Price'}))
    picture1 = forms.URLField(label='Photo1', required=False)
    picture2 = forms.URLField(label='Photo2', required=False)
    picture3 = forms.URLField(label='Photo3', required=False)
    picture4 = forms.URLField(label='Photo4', required=False)
    picture5 = forms.URLField(label='Photo5', required=False)



    class Meta:
        model = SellerMarketPost
        fields = [
            # 'seller',
            'sellcategory',
            'title',
            'description',
            'date_posted',
            'telephone_number',
            'price',
            'picture1',
            'picture2',
            'picture3',
            'picture4',
            'picture5',
        ]
        # fields = '__all__'
        # exclude = ('seller',)
