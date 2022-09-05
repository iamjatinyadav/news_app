from django.db import models
from django_extensions.db.models import TimeStampedModel

from .choices import NEWS_CATEGORY_CHOICES
from user.models import User


# Create your models here.

class Contact(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = 'contact'

    def __str__(self):
        return self.name


class News(TimeStampedModel):
    category = models.CharField(max_length=50, null=True, blank=True, choices=NEWS_CATEGORY_CHOICES, default='Business')
    heading = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    news_cover = models.FileField(upload_to='media/')
    slug = models.CharField(max_length=500, null=True, blank=True)
    views = models.IntegerField(default=0)
    news = models.TextField()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = 'News'

    def __str__(self):
        return self.heading

    @property
    def total_comment_count(self):
        total_comment = self.comments.all().count()
        for comment in self.comments.all():
            total_comment += comment.comment_count
        return total_comment


class Comment(TimeStampedModel):
    news = models.ForeignKey(News, related_name="comments", on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    website = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()

    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comment"

    def __str__(self):
        return self.name + " Comment on " + self.news.heading

    @property
    def comment_count(self):
        return self.subcomments.all().count()



class Newsletter(TimeStampedModel):
    email = models.EmailField(max_length=255)

    class Meta:
        verbose_name_plural = "Newsletter Email"

    def __str__(self):
        return self.email


class SubComment(TimeStampedModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="subcomments")
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    website = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()

    class Meta:
        verbose_name = "SubComments"
        verbose_name_plural = "SubComments"

    def __str__(self):
        return self.name + " Comment on " + self.comment.name + " comments "
