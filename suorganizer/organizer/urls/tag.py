from django.conf.urls import url
from ..views import TagDelete, TagList, TagPageList, tag_detail, tag_list, tag_create, TagCreate, TagUpdate
from ..utils import DetailView
from ..models import Tag

urlpatterns = [
    url(r'^$', TagList.as_view(), name='organizer_tag_list'),
    url(r'^(?P<page_number>\d+)/$', TagPageList.as_view(), name='organizer_tag_page'),
    url(r'^create/$', TagCreate.as_view(), name='organizer_tag_create'),
    url(r'^(?P<slug>[\w\-]+)/$', DetailView.as_view(
        context_object_name='tag', model=Tag, template_name=(
            'organizer/tag_detail.html'
        )
    ), name='organizer_tag_detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(), name='organizer_tag_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', TagDelete.as_view(), name='organizer_tag_delete'),
]

# To Do: 17.2.3 Anticipating Behavior Overrides