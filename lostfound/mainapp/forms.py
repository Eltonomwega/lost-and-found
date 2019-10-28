from django import forms
from .models import Post, Claim
from django.forms import ModelForm,CharField
from bootstrap_datepicker_plus import DateTimePickerInput


CATEGORY_CHOICES = [
    ('Laptops'),
    ('Stationery'),
    ('Phones'),
    ('IDs'),
    ('Wallet & Purses'),
    ('Others'),
]



class Posts(forms.ModelForm):
    
     class Meta:
        model = Post
        fields = ('title','category','description','location','When','image',)
        widgets = {
            'When': DateTimePickerInput(),
        }
        category = forms.MultipleChoiceField(required=True,widget=forms.CheckboxInput,choices=CATEGORY_CHOICES,)

        def __init__(self, *args, **kwargs):
            super(Posts, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class' : 'myfieldclass','color':'black',})


""" Date_From = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            }
        ),
    )

     Date_To = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            }
        ),
    )"""

class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        widgets = {
            'description':forms.Textarea(attrs={'placeholder': "Outline your item's unique features!"}),
            'location':forms.TextInput(attrs={'placeholder': "Where did you lose your item at? Be as specific as possible!"}),
            'time_from':forms.TextInput(attrs={'placeholder': 'Time of loss.. Between this time.. e.g. 11:00'}),
            'time_to':forms.TextInput(attrs={'placeholder': '..and this time.. e.g. 12:00'})
        }
        fields = ['description','location','date_of_loss','image']

        
        