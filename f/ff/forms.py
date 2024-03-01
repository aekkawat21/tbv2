from django import forms
from ff.models import Course


class EditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']