from django.contrib.auth.forms import AuthenticationForm
from compte.models import Enseignant
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column	
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelForm,Textarea,DateField,CheckboxInput,RadioSelect,Select

class  enseignant_form_Register(ModelForm):
    class Meta:
        choice=[('1','Homme'),('2','Femme')]
        model = Enseignant
        fields = ['enseignant_nom' , 'enseignant_prenom','enseignant_naissance','enseignant_lieu','enseignant_adresse','enseignant_sexe','enseignant_email','enseignant_telephone','enseignant_etablissement']
        widgets= {
            'enseignant_naissance':DatePickerInput(format='%d/%m/%Y'),  
            'enseignant_sexe':Select(choices=choice),
            'enseignant_adresse':Textarea(),
            'enseignant_adresse':Textarea(attrs={'rows':4,'cols':80})
        }
        labels = {
               'enseignant_nom': _('Nom:'),
               'enseignant_prenom': _('Prénom:'),
               'enseignant_naissance': _('Date de naissance:'),
               'enseignant_lieu': _('Lieu de naissance:'),
               'enseignant_adresse':_('Adresse:'),
               'enseignant_sexe': _('Sexe:'),
               'enseignant_email': _('Email:'),
               'enseignant_telephone': _('Téléphone:'),
               'enseignant_etablissement': _('Etablissement:'),
    
               }


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('enseignant_nom', css_class='form-group col-md-3 mb-0'),
               Column('enseignant_prenom', css_class='form-group col-md-3 mb-0'),
               Column('enseignant_sexe', css_class='form-group col-md-3 mb-0'), 
               css_class='form-row'
              ),
              Row(
               Column('enseignant_naissance', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_lieu', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_adresse', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('enseignant_email', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_telephone', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_etablissement', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
     Submit('submit', 'Enregistrer')
     ) 

class  enseignant_form_Update(ModelForm):
    class Meta:
        choice=[('1','Homme'),('2','Femme')]
        model = Enseignant
        fields = ['enseignant_nom' , 'enseignant_prenom','enseignant_naissance','enseignant_lieu','enseignant_adresse','enseignant_sexe','enseignant_email','enseignant_telephone','enseignant_etablissement']
        widgets= {
            'enseignant_naissance':DatePickerInput(format='%d/%m/%Y'),  
            'enseignant_sexe':Select(choices=choice),
            'enseignant_adresse':Textarea(attrs={'rows':4,'cols':80})
        }
        labels = {
               'enseignant_nom': _('Nom:'),
               'enseignant_prenom': _('Prénom:'),
               'enseignant_naissance': _('Date de naissance:'),
               'enseignant_lieu': _('Lieu de naissance:'),
               'enseignant_adresse':_('Adresse:'),
               'enseignant_sexe': _('Sexe:'),
               'enseignant_email': _('Email:'),
               'enseignant_telephone': _('Téléphone:'),
               'enseignant_etablissement': _('Etablissement:'),
    
               }


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('enseignant_nom', css_class='form-group col-md-3 mb-0'),
               Column('enseignant_prenom', css_class='form-group col-md-3 mb-0'),
               Column('enseignant_sexe', css_class='form-group col-md-3 mb-0'), 
               css_class='form-row'
              ),
              Row(
               Column('enseignant_naissance', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_lieu', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_adresse', css_class='form-group col-md-4 mb-0'), 
               css_class='form-row'
              ),
              Row(
               Column('enseignant_email', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_telephone', css_class='form-group col-md-4 mb-0'),
               Column('enseignant_etablissement', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
     Submit('submit', 'Enregistrer')
     ) 
