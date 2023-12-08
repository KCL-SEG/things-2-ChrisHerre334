"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing
from django.core.validators import MaxLengthValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    description = forms.CharField(
        widget=forms.Textarea,
        validators=[MaxLengthValidator(limit_value=120)]
    )
    quantity = forms.IntegerField(widget=forms.NumberInput)