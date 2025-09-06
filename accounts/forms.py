from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date
from accounts.models import Profiles

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name" )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = ""  
        self.fields["password2"].help_text = ""  
        self.fields["password1"].widget.attrs['placeholder'] = 'Password (min. 8 characters, letters & numbers)'
        self.fields["password2"].widget.attrs['placeholder'] = 'Repeat password'
        self.fields["email"].widget.attrs['placeholder'] = 'you@example.com'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()

        return user
    
class ProfileEditForm(forms.Form):

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name'
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com'
        })
    )
    
    avatar = forms.ImageField(
        required = False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )
    
    telephone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+380-XX-XXX-XX-XX',
            'pattern': r'[\d\s\-\+\(\)]+',
            'title': 'Only numbers, space, dashes, plus, brackets'
        })
    )
    
    dio = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'write about yourself'
        })
    )
    
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        
        if not self.is_bound:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
            
            if hasattr(user, 'profile'):
                profile = user.profile
                self.fields['telephone'].initial = profile.telephone
                self.fields['dio'].initial = profile.bio
                self.fields['birth_date'].initial = profile.birth_date
                
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.user.pk).exists():
            raise ValidationError("A user with this email already exists.")

        return email

    def clean_telephone(self):
        phone = self.cleaned_data.get('telephone', '')
        if phone:
            digits_only = ''.join(filter(str.isdigit, phone))
            if len(digits_only) < 10:
                raise ValidationError('The phone number is too short.')

        return phone
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date:
            today = date.today()
            if birth_date > today:
                raise ValidationError('Date of birth cannot be in the future.')

            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            if age > 120:
                raise ValidationError('Please check that your date of birth is correct.')

        return birth_date
    
    def save(self):

        self.user.first_name = self.cleaned_data['first_name']
        self.user.last_name = self.cleaned_data['last_name']
        self.user.email = self.cleaned_data['email']
        self.user.save()
        
        profile, created = Profiles.objects.get_or_create(user=self.user)

        profile.telephone = self.cleaned_data.get('telephone', '')
        profile.bio = self.cleaned_data.get('bio', '')
        profile.birth_date = self.cleaned_data.get('birth_date')
        
        if self.cleaned_data.get('avatar'):
            profile.avatar = self.cleaned_data['avatar']
        
        profile.save()
        return self.user