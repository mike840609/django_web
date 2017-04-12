"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


"""
^ 表示文本的开始
$ 表示文本的结束
\d 表示数字
+ 表示前面的元素应该重复至少一次
() 用来捕捉模式中的一部分

"""

#  記得 import include
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #  redrict the empty url to blog.urls
    # 写正则表达式时，记得把一个 r 放在字符串的前面。 
    # 这告诉 Python，这个字符串中的特殊字符是为正则表达式准备的，而不是为 Python 自身准备的。
    
    url(r'', include('blog.urls')),

]
