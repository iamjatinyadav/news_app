import email
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model


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
        fields =('email', 'first_name', 'last_name', 'password')
    
    

    # def clean(self):
    #     super(RegisterForm, self).clean()

    #     email = self.cleaned_data['email']
    #     # pass1 = self.cleaned_data['pass1']
    #     # pass2 = self.cleaned_data['pass2']

    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError( "this email is already registerd....")
        
    #     if pass1 != pass2:
    #         raise forms.ValidationError("password and confirm password not same")

    #     return self.cleaned_data

    # def is_valid(self, request):
    #     email = self.data['email']
    #     fname = self.data['fname']
    #     lname = self.data['lname']
    #     pass1 = self.data['pass']
    #     pass2 = self.data['pass2']

    #     if User.objects.filter(email=email).exists():
    #         return messages.error(request, "user is already register")
    #     if pass1 != pass2:
    #         return messages.error(request, "password and confirm password not match..")
    #     data = {
    #         "email": email,
    #         "first_name": fname,
    #         "last_name": lname,
    #     }
    #     return data

    
    # def save(self, commit=True):
    #     user_obj = super(RegisterForm, self).save(commit=False)
    #     #user_obj.email = self.cleaned_data['email']
    #     user_obj = User.objects.create(**self.data)
    #     user_obj.set_password(self.cleaned_data['pass'])
    #     if commit:
    #         user_obj.save()
    #     return user_obj
        
     

# User = get_user_model()
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
    
    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('pass')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("this email does not exist...")
        if not user.check_password(password):
            raise forms.ValidationError("Invalid Password...")
        if not user.is_active:
            raise forms.ValidationError("this user no longer active..")

        return super(LoginForm, self).clean(*args, **kwargs)
   


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
        

    





