from django.contrib.auth.forms import AuthenticationForm
from compte.models import Note
from django.forms import ModelForm ,Textarea
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column	
from bootstrap_datepicker_plus import DatePickerInput


class note_register_form(ModelForm):
    class Meta:
        model = Note
        fields = ['titre' , 'date_note' , 'sujet' , 'classe','enseignant']
        labels = {
               'titre': _('titre de la note:'),
               'date_note': _('date:'),
               'sujet': _('note:'),
               'classe': _('classe:'),
               'enseignant':_('Enseigant:'),
               }
        widgets= {'sujet':Textarea(),
                   'date_note':DatePickerInput(format='%d/%m/%Y'),
        }

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('titre', css_class='form-group col-md-4 mb-0'),
               Column('date_note', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('sujet', css_class='form-group col-md-8 mb-0'),
               css_class='form-row'
          ),
          Row(
               Column('classe', css_class='form-group col-md-4 mb-0'),
               Column('enseignant', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
    Submit('submit', 'Enregistrer')
     ) 



class note_update_form(ModelForm):
    class Meta:
        model = Note
        fields = ['titre' , 'date_note' , 'sujet' , 'classe','enseignant']
        labels = {
               'titre': _('titre de la note:'),
               'date_note': _('date:'),
               'sujet': _('note:'),
               'classe': _('classe:'),
               'enseignant':_('Enseigant:'),
               }
        widgets= {'sujet':Textarea(),
                   'date_note':DatePickerInput(format='%d/%m/%Y'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
               Column('titre', css_class='form-group col-md-4 mb-0'),
               Column('date_note', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
            Row(
               Column('sujet', css_class='form-group col-md-8 mb-0'),
               css_class='form-row'
             ),
            Row(
               Column('classe', css_class='form-group col-md-4 mb-0'),
               Column('enseignant', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
            ),
    Submit('submit', 'Enregistrer')
    ) 

class note_read_form(ModelForm):
    class Meta:
        model = Note
        fields = ['titre' , 'date_note' , 'sujet' , 'classe']
        labels = {
               'titre': _('titre de la note:'),
               'date_note': _('date:'),
               'sujet': _('note:'),
               'classe': _('classe:'),
               }
        widgets= {'sujet':Textarea(),
                   'date_note':DatePickerInput(format='%d/%m/%Y'),
                   
        
        }

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.layout = Layout(
              Row(
               Column('titre', css_class='form-group col-md-4 mb-0'),
               Column('date_note', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
              ),
              Row(
               Column('sujet', css_class='form-group col-md-8 mb-0'),
               css_class='form-row'
          ),
          Row(
               Column('classe', css_class='form-group col-md-4 mb-0'),
               css_class='form-row'
          ),
     ) 