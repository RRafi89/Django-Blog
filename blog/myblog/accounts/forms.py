from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'autocomplete': 'email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password'
        })
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError(
                    "Please enter a correct email and password. Note that both fields may be case-sensitive."
                )
            elif not self.user.is_active:
                raise forms.ValidationError("This account is inactive.")
        
        return self.cleaned_data

    def get_user(self):
        return self.user if hasattr(self, 'user') else None


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize password fields
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password'
        })
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email

# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    password = None
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter current password to save changes'
        }),
        required=True
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    profile_image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        }),
        required=False
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tell us about yourself',
            'rows': 4
        }),
        required=False
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        required=False
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        }),
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'profile_image', 
                 'bio', 'date_of_birth', 'phone_number')

    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not self.instance.check_password(current_password):
            raise forms.ValidationError('Incorrect password')
        return current_password