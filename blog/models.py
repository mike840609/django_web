from django.db import models
from django.utils import timezone

# Create your models here.
# means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model):
    
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)

    # named rule:
    # we use lowercase and underscores instead of spaces
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # In this scenario, when we call __str__() we will get a text (string) with a Post title.
    def __str__(self):
        return self.title


# Create tables for models in your database

# check before migrate
# $: python manage.py makemigrations blog

# migrate
# $: python manage.py migrate blog
