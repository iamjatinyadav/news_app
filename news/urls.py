from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name="index"),
    #path('catagory/<str:category>', views.category, name="category"),
    path('single_news/<slug:slug>', views.singlenews, name="single_news"),
    path('singlenews', views.singlenews, name="single_news"),
    path('contact', views.contact, name="contact"),
    path('Login',views.handlelogin, name="login"),
    path('Register', views.handleregister, name="register"),
    path('Logout', views.handlelogout, name="logout"),
    # path('comment', views.comment, name="comment"),
    path('search', views.search, name="search"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('subcomment', views.handlesubcomment, name="subcomment"),

    #class base urls
    path('', views.IndexView.as_view(), name="index"),
    path('catagory/<str:category>', views.CategoryView.as_view(), name="category"),

]