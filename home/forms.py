from django import forms

class ContactForm(forms.Form):
    your_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

