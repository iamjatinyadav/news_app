from django import forms
from news.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.isalpha():
            raise forms.ValidationError("name only in alphabetic")
        return name

    def clean_message(self):
        message = self.cleaned_data["message"]

        if len(message) < 5:
            raise forms.ValidationError("minimum use 5 characters")
        return message


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'news', 'website', 'message' )


class SubCommentForm(forms.ModelForm):
    class Meta:
        model = SubComment
        fields = ('name', 'email', 'comment', 'website', 'message' )


class RegisterForm(forms.ModelForm):
    class Meta:
        model= User
        fields =('first_name', 'last_name', 'email', 'password')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')


