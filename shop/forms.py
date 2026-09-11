from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'query']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'contact-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+91 98765 43210',
                'class': 'contact-input',
                'type': 'tel',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'class': 'contact-input',
            }),
            'query': forms.Textarea(attrs={
                'placeholder': 'Tell us how we can help you...',
                'class': 'contact-input',
                'rows': 5,
            }),
        }
