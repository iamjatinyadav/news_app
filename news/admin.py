from django.contrib import admin

# Register your models here.

from .models import Contact, News, Comment, Newsletter, SubComment


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email", "created"]


admin.site.register(Newsletter, NewsletterAdmin)


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ["name", "subject", "created", "modified"]


class NewsAdmin(admin.ModelAdmin):
    list_display = ["heading", "category", "created", "modified"]


admin.site.register(News, NewsAdmin)


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ["name", "created", "modified"]

# @admin.register(NewsViews)
# class NewsViewsCount(admin.ModelAdmin):
#     list_display = ["view", "created", "modified"]


@admin.register(SubComment)
class SubCommentAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]