from django import forms
from .models import Credentials


class CredentialsForm(forms.ModelForm):

    class Meta:
        model = Credentials
        fields = ('client_id', 'api_key',)