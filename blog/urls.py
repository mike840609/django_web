from django.conf.urls import url
from . import views

# As you can see, we're now assigning a view called post_list
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]