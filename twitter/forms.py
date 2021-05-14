from django import forms
from .models import twitter


class TwitterForm(forms.ModelForm):
    class Meta:
        model = twitter
        fields = '__all__'
