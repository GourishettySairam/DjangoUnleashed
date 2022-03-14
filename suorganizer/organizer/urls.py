from django.conf.urls import url, include
from .views import tag_detail, tag_list, startup_list, startup_detail
from blog import urls as blog_urls

urlpatterns = [
    url(r'^tag/$', tag_list, name='organizer_tag_list'),
    url(r'tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    url(r'startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    url(r'^blog/', include(blog_urls)),
]