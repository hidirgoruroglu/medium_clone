from django.forms import forms

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("En az 3 karakter olmalı...")