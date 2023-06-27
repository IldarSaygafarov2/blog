from django import forms

from .models import Article, User, CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title', 'content', 'photo', 'ingredients', 'steps', 'is_published', 'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Название', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'placeholder': 'Описание', 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'Ингредиенты', 'class': 'form-control'}),
            'steps': forms.Textarea(attrs={
                'placeholder': 'Приготовление', 'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


class CustomUserRegister(UserCreationForm):
    username = forms.CharField(max_length=255,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя'
                               })
                               )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            })
        }


