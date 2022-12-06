from django import forms
from django.core import validators
# from first_app.models import Album, Musician
from first_app import models

class Musician_form(forms.ModelForm):
    # """Form definition for MODELNAME."""
    class Meta:
        # """Meta definition for MODELNAMEform."""
        model = models.Musician
        fields = "__all__"  #for all fields
        # exclude = ['first_name']    # if you want to remove a field
        # fields = ('first_name', 'last_name') # if you want to keep some

        
# till 3.7 videos
# def even_or_odd(value):
#     if value % 2  == 1:
#         raise forms.ValidationError("enter a even number")

# #forms is library, Form is base class of the library

# class user_form(forms.Form):
    # num_val = forms.IntegerField(validators=[even_or_odd])

   


    # <input type="text" name="name" value="" required>
#     user_name = forms.CharField(required=False, label="Your Name", label_suffix="=>", 
#     widget=forms.TextInput(attrs={'style': 'width: 200px', 'placeholder': 'Your Name'} ) )
#     user_dob = forms.DateField(label='Date Of Birth', widget=forms.TextInput(
#         attrs= {'type': 'date', 'style': 'width:200px'}
#     ))
#     user_email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder': 'Your Email', 'style': 'width:200px' }))

#     user_pass = forms.CharField(max_length=15, min_length=5)

#     # choice
#     country = (('', 'Select Country'),('BD','Bangladesh'),('IND','India'), ('Pak', 'Pakistan'))
#     nationality = forms.ChoiceField(choices=country)

#     # radio
#     born = forms.ChoiceField(choices=country, widget=forms.RadioSelect)

#     # multiple choice
#     number = (('1','one'), ('2','two'), ('3','three'))
#     fav_num = forms.MultipleChoiceField(choices=number)

    
#     # validators
#     cat_name = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(10)])
   
#    # boolean
#     boolean_field = forms.BooleanField(required=False, label="Are you accepting our terms & conditions")

    # # email verify
    # user_email = forms.EmailField()
    # user_vmail = forms.EmailField()

    # def clean(self):
    #     all_clean_data = super().clean()

    #     user_email = all_clean_data['user_email']
    #     user_vmail = all_clean_data['user_vmail']

    #     if user_email != user_vmail:
    #         raise forms.ValidationError("email is not same")
