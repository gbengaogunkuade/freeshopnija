from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from visitor.models import UserProfile







# USER REGISTRATION FORM
# - create a new form "FreeShopUserForm" from the
# - builtin "UserCreationForm" of the builtin model "User"
# - make sure to exclude the password1 and password2 fields from the form creation for security reasons
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder':'Enter your Username'}))
    first_name = forms.CharField(label='FirstName', widget=forms.TextInput(attrs={'placeholder':'Enter your FirstName'}))
    last_name = forms.CharField(label='LastName', widget=forms.TextInput(attrs={'placeholder':'Enter your LastName'}))
    email = forms.CharField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder':'Enter your Email Address'}))
    verify_email = forms.CharField(label='Verify Your Email Address', widget=forms.EmailInput(attrs={'placeholder':'Verify your Email Address'}))



    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'password1',
            'password2'
        ]







# USER EDIT FORM
# - create a new form "UserEditForm" to edit the
# - details of the builtin model "User"
class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']








# USER PROFILE UPDATE FORM
# - create a new form "UserProfileForm" from "UserProfile" model
# - this will be later joined to the "UserEditForm" above
# - to update the user profile of registered users
class UserProfileForm(forms.ModelForm):
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'placeholder':'Enter your Company Name'}))
    delivery_address = forms.CharField(label='Delivery Address', widget=forms.Textarea(attrs={'placeholder':'Enter your Delivery Address'}))
    telephone_number = forms.CharField(label='Phone Number', widget=forms.NumberInput(attrs={'placeholder':'Enter your Phone Number'}))
    profile_picture_1 = forms.ImageField(label='First Profile Photo')
    profile_picture_2 = forms.ImageField(label='Second Profile Photo')


    class Meta:
        model = UserProfile
        fields = [
            'company_name',
            'delivery_address',
            'telephone_number',
            'profile_picture_1',
            'profile_picture_2'
        ]
















