from django import forms
from .models import twitter
from .models import update


class TwitterForm(forms.ModelForm):
    class Meta:
        model = twitter
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    class Meta:
        model = twitter
        fields = '__all__'
