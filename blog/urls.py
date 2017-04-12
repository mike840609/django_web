from django.conf.urls import url
from . import views

# As you can see, we're now assigning a view called post_list
urlpatterns = [
    #  call post_list function
    url(r'^$', views.post_list, name='post_list'),

    # \d  also tells us that it can only be a digit, not a letter (so everything between 0 and 9)
    #  +  means that there needs to be one or more digits there
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]