from django.contrib.auth.forms import AuthenticationForm
from compte.models import Etablissement ,Classe ,Profile
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column	



class classe_form_register(ModelForm):
    class Meta:
        model = Classe
        fields = ['classe_code','classe_desig']
        labels = {
               'classe_code': _('etablissement:'),
               'classe_desig': _('classe Designation:'),
               }


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('classe_code', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('classe_desig', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
    Submit('submit', 'Enregistrer')
     )


class classe_form_Updater(ModelForm):
    class Meta:
        model = Classe
        fields = ['classe_code','classe_desig']
        labels = {
               'classe_code': _('etablissement:'),
               'classe_desig': _('classe Designation:'),
               }


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('classe_code', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('classe_desig', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
    Submit('submit', 'Enregistrer')
     )
