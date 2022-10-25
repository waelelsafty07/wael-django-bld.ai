from django import forms
from .models import Students
from django.forms import ValidationError


def check_mark(value):
    if value < 0:
        raise ValidationError('Mark must be greater than 0')


class StudentForm(forms.ModelForm):
    # validates if sent in request, if True: should send a value to validate on it
    mark = forms.IntegerField(required=False, validators=[check_mark])

    class Meta:
        model = Students
        fields = "__all__"
