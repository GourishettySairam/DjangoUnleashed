from django.conf.urls import url
from .views import PostArchiveMonth, PostArchiveYear, PostList, post_detail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    url(r'^$', 
        PostList.as_view(template_name='blog/post_list.html'),
        name="blog_post_list"),
    url(r'^create/$',
        PostCreate.as_view(),
        name='blog_post_create'
    ),
    url(r'^(?P<year>\d{4})/'
    r'(?P<month>\d{1,2})/'
    r'(?P<slug>[\w\-]+)/$',
        post_detail,
        {'parent_template': 'base.html'},
        name="blog_post_detail"),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'update/$',
        PostUpdate.as_view(),
        name="blog_post_update"),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'delete/$',
        PostDelete.as_view(),
        name="blog_post_delete"
    ),
    url(r'^(?P<year>\d{4})/$',
        PostArchiveYear.as_view(),
        name='blog_post_archive_year'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/$',
        PostArchiveMonth.as_view(),
        name="blog_post_archive_month"
    )
]