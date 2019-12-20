from django.contrib.auth.forms import AuthenticationForm
from . models import Etablissement ,Classe ,Profile
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column	



class User_Form(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Mot de passe',max_length=32, widget=forms.PasswordInput)
    conf_password = forms.CharField(label='Confirmation Password',max_length=32, widget=forms.PasswordInput)
    etablissement = forms.ModelChoiceField(Etablissement.objects.all(), label='Etablissement',to_field_name="structure_desig")
    
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('username', css_class='form-group col-md-4 mb-0'),
               Column('etablissement', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('password', css_class='form-group col-md-4 mb-0'),
               Column('conf_password', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
    Submit('submit', 'Enregistrer')
     )


'''
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password',max_length=32, widget=forms.PasswordInput)
    conf_password = forms.CharField(label='Confirm Password',max_length=32, widget=forms.PasswordInput)
    structure = forms.ModelChoiceField(Structure.objects.all(), to_field_name="structure_desig")
'''