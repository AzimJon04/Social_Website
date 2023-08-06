from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import UserProfile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'telegram_link', 'image']
        # Указываем виджет для поля 'image' (FileInput)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }


# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
