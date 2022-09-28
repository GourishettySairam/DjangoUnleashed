"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import urls as auth_urls

from organizer.urls import  (
    startup as startup_urls,
    tag as tag_urls
)
from .views import redirect_root
from contact import urls as contact_urls
from blog import urls as blog_urls
from django.views.generic import RedirectView, TemplateView
from user import urls as user_urls

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(
        template_name='site/about.html'
    ), name='about_site'),
    path('admin/', admin.site.urls),
    url(r'^blog/', include(blog_urls)),
    url(r'^startup/', include(startup_urls)),
    url(r'^tag/', include(tag_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^$', RedirectView.as_view(
        pattern_name='blog_post_list',
        permanent=False
    )),
    url(r'^user/', include(user_urls,
        namespace='dj-auth'
        )
    ),
]

# username: sairam, password: sairam