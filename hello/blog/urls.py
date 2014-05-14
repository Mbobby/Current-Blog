from django.conf.urls import patterns, include, url
from blog.views import all, get_article, create, like

urlpatterns = patterns('',
	url(r'^all/$',all ),
	url(r'^get_article/(?P<article_id>\d+)/$', get_article),
	url(r'^create/' , create),
	url(r'^like/(?P<article_id>\d+)/$', like), 
	url(r'^month_query/(?P<month_num>\d+)/$', 'blog.views.month_query'), 	

)
