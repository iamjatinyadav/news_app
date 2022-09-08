from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name="index"),
    #path('catagory/<str:category>', views.category, name="category"),
    #path('single_news/<slug:slug>', views.singlenews, name="single_news"),
    #path('singlenews', views.singlenews, name="single_news"),
    #path('contact', views.contact, name="contact"),
    #path('Login',views.handlelogin, name="login"),
    #path('Register', views.handleregister, name="register"),
    #path('Logout', views.handlelogout, name="logout"),
    #path('search', views.search, name="search"),
    #path('newsletter', views.newsletter, name="newsletter"),
    #path('subcomment', views.handlesubcomment, name="subcomment"),

    #class base urls
    path('', views.IndexView.as_view(), name="index"),
    path('catagory/<str:category>', views.CategoryView.as_view(), name="category"),
    path('single_news/<slug:slug>', views.SingleNewsView.as_view(), name="single_news"),
    path('singlenews', views.SingleNewsView.as_view(), name="single_new"),
    path('comment', views.CommentPostView.as_view(), name="comments"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('Login', views.HandleLoginView.as_view(), name="login"),
    path('Register', views.HandleRegisterView.as_view(), name="register"),
    path('Logout', views.HandleLogout.as_view(), name="logout"),
    path('search', views.SearchView.as_view(), name="search"),
    path('newsletter', views.NewsLetterFormView.as_view(), name="newsletter"),
    path('subcomment', views.HandleSubCommentView.as_view(), name="subcomment"),

]