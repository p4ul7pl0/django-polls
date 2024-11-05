from django import forms
from .widgets import PasswordInput

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
FAVORITE_COLORS_CHOICES = {"blue": "Blue", "white": "White"}
CHOICES = {"1": "First", "2": "Second"}

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            "all": ["pretty.css"],
        }
        js = ["animations.js", "actions.js"]

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={"size": "40"}))
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )


class MyForm(forms.Form):
    test = forms.CharField(widget=PasswordInput(left_icon="bi bi-alarm-fill"))