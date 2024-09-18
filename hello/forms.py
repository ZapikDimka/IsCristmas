
from django import forms

class AddParticipantForm(forms.Form):
    participant = forms.CharField(label="Ім'я учасника", max_length=100)
