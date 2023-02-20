from django import forms
from .models import Profile, Message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('external_id', 'name')
        widgets = {'name': forms.TextInput}


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('profile', 'text')
        widgets = {'text': forms.TextInput}