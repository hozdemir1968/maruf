from django import forms
from .models import Announce


class AnnounceForm(forms.ModelForm):

    class Meta:
        model=Announce
        fields=[
            'title',
            'content',
        ]
    