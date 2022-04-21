from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    tel = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "email", "tel", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.tel = self.cleaned_data['tel']
        if commit:
            user.save()
        return user
