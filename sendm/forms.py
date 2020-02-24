from django import forms
from sendm.models import Mail

class MailForm(forms.ModelForm):

    
    class Meta:
        model = Mail
        fields = '__all__'
        # fields = {'text', 'email'}