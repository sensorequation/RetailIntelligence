__author__ = 'vivek'

from django import forms

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

class SearchForm(forms.Form):
   searchfield= forms.CharField(max_length = 100)

class UserProfileAddForm(forms.Form):
    Username=forms.CharField(max_length = 100)
    '''
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    =forms.CharField(max_length = 100)
    '''