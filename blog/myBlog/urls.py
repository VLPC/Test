from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', posts_list, name='posts_list'),
	url(r'post/(?P<pk>\d+)/$', PostDetails.as_view(), name='post_detail'),
	url(r'tags/$', tags_list, name='tags_list'),
	url(r'tag/(?P<pk>\d+)/$', TagDetails.as_view(), name='tag_detail'),
	url(r'tag/create/$', TagCreate.as_view(), name='tag_create'),
	url(r'post/create/$', PostCreate.as_view(), name='post_create'),
	url(r'tag/(?P<pk>\d+)/update/$', TagUpdate.as_view(), name='tag_update'),
	url(r'post/(?P<pk>\d+)/update/$', PostUpdate.as_view(), name='post_update'),
	url(r'post/(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post_delete'),
	url(r'tag/(?P<pk>\d+)/delete/$', TagDelete.as_view(), name='tag_delete')
]
