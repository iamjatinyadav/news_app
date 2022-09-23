from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from news.models import News, User, Newsletter,Comment, SubComment
from .forms import ContactForm, CommentForm, RegisterForm, SubCommentForm, LoginForm, NewsletterForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm

#for class base view

from django.views.generic import ListView, DetailView, CreateView, FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from .choices import NEWS_CATEGORY_CHOICES



# Create your views here.
"""
def index(request):
    latest_news = News.objects.filter().order_by('-id')[:2]
    news = News.objects.order_by('id')
    context = {'latest_news': latest_news,'news': news,}
    return render(request, 'news/index.html', context)
"""


class IndexView(ListView):
    model = News
    template_name = 'news/index.html'

    def get_context_data(self, *args, **kwargs):
        et = super(IndexView, self).get_context_data(**kwargs)
        et['latest_news'] = News.objects.filter().order_by('-id')[:2]
        et['news'] = News.objects.order_by('id')
        return et

"""
def category(request, category):
    if category == "business":
        news = News.objects.filter(category="Business")
    else:
        news = News.objects.filter(category=category)
    context = {'news': news}
    return render(request, 'news/category.html', context)
"""
class CategoryView(ListView):
    template_name = "news/category.html"

    def get(self, request, *args, **kwargs):
        news = News.objects.filter(category=kwargs.get('category'))
        # if kwargs.get('category') == NEWS_CATEGORY_CHOICES.Business:
        #     news = News.objects.filter(category=NEWS_CATEGORY_CHOICES.Business)
        return render(request, self.template_name, {'news': news})


"""
def singlenews(request, slug):
    single_news = News.objects.get(slug=slug)
    total_comment = single_news.total_comment_count
    single_news.views = single_news.views + 1
    single_news.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('single_news', slug=slug)

    context = {'single_news': single_news, 'total_comments': total_comment}
    return render(request, 'news/single.html', context)
"""


class SingleNewsView(DetailView):
    model = News
    template_name = "news/single.html"

    def get(self, request, *args, **kwargs):
        single_news = News.objects.get(slug=kwargs.get('slug'))
        total_comment = single_news.total_comment_count
        single_news.views = single_news.views + 1
        single_news.save()

        context = {'single_news': single_news, 'total_comments': total_comment}
        return render(request, 'news/single.html', context)


class CommentPostView(CreateView):
    form_class = CommentForm
    template_name = "news/single.html"
    # success_url = '/single_news/{{single_news}}'

    def get_success_url(self):
        current_slug = self.object.news.slug
        return reverse_lazy('single_news', kwargs={'slug': current_slug})


    # def get(self, request, *args, **kwargs):
    #     form = CommentForm()
    #     context = {'form': form}
    #     return render(request, "news/single.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = CommentForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect(request.META['HTTP_REFERER'])

"""
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'news/contact.html', context)
"""


class ContactView(CreateView):
    form_class = ContactForm
    template_name = "news/contact.html"
    success_url = reverse_lazy("index")
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request, "news/contact.html")
    #
    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = ContactForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect("index")
    #         return redirect("contact")


"""
def handlelogin(request):
    if request.method == "POST":
        email=request.POST["email"]
        password = request.POST["pass"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, "news/login.html")
"""


class HandleLoginView(LoginView):
    template_name = "news/login.html"
    #add LOGIN_REDIRECT_URL in base.py
    # authentication_form = LoginForm
    #success_url = "index"

    
    # def post(self, request, *args, **kwargs):
    #     email = request.POST["email"]
    #     password = request.POST["pass"]
    #     user = authenticate(request, email=email, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('index')
    #     else:
    #         return redirect('login')

            # else:
            #     return redirect('login')

            # if not user:
            #     messages =  "this email does not exist..."
            #     print(messages)
            #     context = { messages : messages} 
            #     return render(request, 'news/login.html', context)

            # if not user.check_password(password):
            #     return messages.error(request, "Invalid Password...")
            # if not user.is_active:
            #     return messages.error(request, "this user no longer active..")

        

        # form = LoginForm(request.POST or None)
        # if form.is_valid():
        #     email = form.cleaned_data.get("email")
        #     password = form.cleaned_data.get("pass")
        #     user = authenticate(request, email=email, password=password)
        #     login(request, user)
        #     return redirect("index")


        # return render(request, 'news/login.html', {'form': form})

        

"""
def handleregister(request):
    if request.method == "POST":
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']
        user = User.objects.filter(email=email)
        if user:
            message=("User is already exist")
            context={"message":message}
            return render(request, "news/register.html", context)
        else:
            if pass1 == pass2:
                data = {
                    "email" : email,
                    "first_name": fname,
                    "last_name" : lname,
                }
                user_obj = User.objects.create(**data)
                user_obj.set_password(pass1)
                user_obj.save()
                return redirect('login')
            message=("Password and Re-enter password not matching..")
            context = {"message": message}
            return render(request, "news/register.html", context)

    return render(request, "news/register.html")
"""


class HandleRegisterView(CreateView):
    template_name = "news/register.html"
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        # form = RegisterForm(request.POST)
        # if form.is_valid():
        #     email = request.POST['email']
        #     fname = request.POST['fname']
        #     lname = request.POST['lname']
        #     pass1 = request.POST['pass']
        #      pass2 = request.POST['pass2']
        #     data = {
        #                 "email": email,
        #                 "first_name": fname,
        #                 "last_name": lname,
        #             }
        #     user_obj = User.objects.create(**data)
        #     user_obj.set_password(pass1)
        #     user_obj.save()
        #     return redirect('login')
        # context = {"form": form}
        # return render(request, 'news/register.html', context)


        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.filter(email=email)
        if user:
            message = "User is already exist"
            context = {"message": message}
            return render(request, "news/register.html", context)
        else:
            if pass1 == pass2:
                data = {
                    "email": email,
                    "first_name": fname,
                    "last_name": lname,
                }
                user_obj = User.objects.create(**data)
                user_obj.set_password(pass1)
                user_obj.is_active = True
                user_obj.save()
                return redirect('login')
            message = "Password and Re-enter password not matching.."
            context = {"message": message}
            return render(request, "news/register.html", context)




"""
def handlelogout(request):
    logout(request)
    return redirect("index")
"""


class HandleLogout(LogoutView):
    template_name = "news/index.html"
    # def get(self, request, *args, **kwargs):
    #     logout(request)
    #     return redirect("index")


"""
def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allnews = News.objects.none()
    else:
        allnewstitle = News.objects.filter(heading__icontains=query)
        allnewscontent = News.objects.filter(news__icontains=query)
        allnews = allnewstitle.union(allnewscontent)

    context = {"allnews": allnews, "query": query}
    return render(request, 'news/search.html', context)
"""


class SearchView(ListView):
    template_name = "news/search.html"

    def get(self, request, *args, **kwargs):
        query = request.GET['query']
        if len(query) > 78:
            allnews = News.objects.none()
        else:
            allnewstitle = News.objects.filter(heading__icontains=query)
            allnewscontent = News.objects.filter(news__icontains=query)
            allnews = allnewstitle.union(allnewscontent)

        context = {"allnews": allnews, "query": query}
        return render(request, 'news/search.html', context)

"""
def newsletter(request):
    if request.method == "GET":
        email = request.GET['email']

        news_letter = Newsletter(email=email)
        news_letter.save()
        send_mail(
            'Welcome to biznews NewsLetter',
            f'Welcome, {email}.Thankyou for subscribe our NewsLetter',
            'jatinyadav0000@gmail.com',
            [f'{email}'],
            fail_silently=False,
        )
        return redirect('index')
"""


class NewsLetterFormView(CreateView):
    template_name = "news/newsletter.html"
    form_class = NewsletterForm


    def post(self, request, *args, **kwargs):
        form = NewsletterForm(request.POST)
        if form.is_valid(request):
            form.save()
        return redirect("index")



"""
def handlesubcomment(request):
    if request.method == "POST":
        form = SubCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'news/single.html')
"""


class HandleSubCommentView(CreateView):
    template_name = "news/single.html"
    form_class = SubCommentForm
    # success_url = reverse_lazy("index")

    def get_success_url(self):
        current_slug = self.object.comment.news.slug
        return reverse_lazy('single_news', kwargs={'slug': current_slug})
    # def get(self, request, *args, **kwargs):
    #     return redirect(request.META['HTTP_REFERER'])

    # def post(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         form = SubCommentForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect(request.META['HTTP_REFERER'])
    #         return redirect(request.META['HTTP_REFERER'])

