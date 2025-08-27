from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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
        # self.fields["username"].widget.attrs['placeholder'] = 'Enter username'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email.cleaned_data["email"]
        user.first_name.cleaned_data["first_name"]
        user.last_name.cleaned_data["last_name"]
        if commit:
            user.save()
        return user