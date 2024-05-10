from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CHOICES


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Введите логин',
        required=True, 
        help_text='Обязятельное поле. Не более 150 символов. Нельзя водить символы',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
        
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text="Пароль не долен быть  простым и коротким",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите логин*',
        required=True, 
        help_text='Обязятельное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email',]
        
        
class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Изображение профиля*',
        required=False,
    )
    
    class Meta:
        model = Profile
        fields = ['img']
        
class UserGenderForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=CHOICES, label='Выберите пол*',
    widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['gender']
    
    
class UserChoice(forms.ModelForm):
    boolean = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Соглашение про отправку уведомлений на почту')

    class Meta:
        model = Profile
        fields = ['boolean']
    
    