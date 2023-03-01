from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label="Your email:",
        required=True
    )
    message = forms.CharField(
        label="Message:",
        required=True,
        widget=forms.Textarea,
    )
    captcha = ReCaptchaField(
        label="",
        widget=ReCaptchaV3(),
    )
                          
