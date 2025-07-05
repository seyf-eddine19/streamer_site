from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['firstname', 'lastname', 'email', 'phone_number', 'message']

    def __init__(self, *args, **kwargs):
        lang = kwargs.pop('lang', 'en')
        super().__init__(*args, **kwargs)

        if lang == 'en':
            self.fields['firstname'].widget.attrs.update({'placeholder': 'FIRST NAME', 'class': 'input'})
            self.fields['lastname'].widget.attrs.update({'placeholder': 'LAST NAME', 'class': 'input'})
            self.fields['email'].widget.attrs.update({'placeholder': 'EMAIL ADDRESS', 'class': 'input'})
            self.fields['phone_number'].widget.attrs.update({'placeholder': 'PHONE NUMBER', 'class': 'input'})
            self.fields['message'].widget.attrs.update({'placeholder': 'Write your message here', 'class': 'textarea', 'rows': 4})
        else:
            self.fields['firstname'].widget.attrs.update({'placeholder': 'الاسم الأول', 'class': 'input'})
            self.fields['lastname'].widget.attrs.update({'placeholder': 'الاسم الأخير', 'class': 'input'})
            self.fields['email'].widget.attrs.update({'placeholder': 'البريد الإلكتروني', 'class': 'input'})
            self.fields['phone_number'].widget.attrs.update({'placeholder': 'رقم الهاتف', 'class': 'input'})
            self.fields['message'].widget.attrs.update({'placeholder': 'اكتب رسالتك هنا', 'class': 'textarea', 'rows': 4})