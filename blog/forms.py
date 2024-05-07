from django import forms
from .models import Message

class ContactForm(forms.ModelForm):  
    subject = forms.CharField(
        max_length=200, 
        label='Тема письма*',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Почта*',
        help_text='Обязательное поле',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Текст письма*',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Message 
        fields = ['subject', 'email', 'message']  

    

    