from dataclasses import fields
from email import message
from urllib import request
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
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


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"


    def is_valid(self, request):
        email = self.data['email']

        if Newsletter.objects.filter(email= email).exists():
            return messages.error(request, "this email is already registerd.")

        send_mail(
                'Welcome to biznews NewsLetter',
                f'Welcome, {email}.Thankyou for subscribe our NewsLetter',
                'jatinyadav0000@gmail.com',
                [f'{email}'],
                fail_silently=False,
            )

        return email
        

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     email = Newsletter.objects.filter(email=email)
    #     if email:
    #         raise forms.ValidationError("Already subscribed")
    #     return email





