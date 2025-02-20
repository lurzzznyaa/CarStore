from django import forms
from .models import Car

# {{ form.as_p }}

class CarCreateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('make', 'model', 'image', 'year', 'price', 'description', 'category')


class CarEditForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('make', 'model', 'image', 'year', 'price', 'description', 'category')