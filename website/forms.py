from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100)
    mail = forms.EmailField(required=False)
    message = forms.CharField(min_length=10, widget=forms.Textarea)
