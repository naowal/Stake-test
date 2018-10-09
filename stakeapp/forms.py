from django import forms
from .models import Message

class PushForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']