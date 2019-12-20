from django.contrib.auth.forms import AuthenticationForm
from compte.models import Etablissement ,Classe ,Profile
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column	



class etablissement_form_register(ModelForm):
    class Meta:
        model = Etablissement
        fields = ['etablissement_code','etablissement_desig']
        labels = {
               'etablissement_code': _('Etablissement Code :'),
               'etablissement_desig': _('Etablissement Designation:'),
               }


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('etablissement_code', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('etablissement_desig', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
    Submit('submit', 'Enregistrer')
     )


class etablissement_form_Updater(ModelForm):
    class Meta:
        model = Etablissement
        fields = ['etablissement_code','etablissement_desig']
        labels = {
               'etablissement_code': _('Etablissement Code :'),
               'etablissement_desig': _('Etablissement Designation:'),
               }


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('etablissement_code', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('etablissement_desig', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
    Submit('submit', 'Enregistrer')
     )     