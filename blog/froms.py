from django import forms
from .models import Post
from django.contrib.auth.models import User


class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'image']

    def clean_data(self):
        self.email = self.cleaned_data.get('email')
        self.password2 = self.cleaned_data.get('password2')
        self.password = self.cleaned_data.get('password')
        self.username = self.email.split("@")[0]
        print(self.cleaned_data)
        if self.email and User.objects.filter(email=self.email).exists():
            raise forms.ValidationError('This email address is already in use.')
        if not self.password2:
            raise forms.ValidationError("Password field is required")
        if len(self.password2) < 8: 
            raise forms.ValidationError("Password too short")
        if self.password2 and self.password and self.password != self.password2:
            raise forms.ValidationError('Passwords do not match.')

    def save(self, commit=True):
        self.clean_data()
        user = User()
        user.email = self.email
        user.set_password(self.password)
        user.username = self.username
        if commit:
            user.save()
        if self.cleaned_data.get('image'):
            image = self.cleaned_data['image']
            user.image = image
            user.save()
        return user
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


    
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'content', 'image')

