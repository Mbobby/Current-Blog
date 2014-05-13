from django.shortcuts import render_to_response
from blog.models import Article
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

#importing the form
from blog.forms import ArticleForm

# Create your views here.


def all(request):
	return render_to_response('all.html',{'articles':Article.objects.all().order_by('-pub_date') })


def get_article(request, article_id):
	return render_to_response('get.html', {'article': Article.objects.get(id = article_id)})


def create(request):
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog/all')
	c = {}
	c.update(csrf(request))
	c['form'] = ArticleForm()
	return render_to_response('create.html', c)

def like(request, article_id):
	l = Article.objects.get(id = article_id)
	l.likes = l.likes + 1
	l.save()
	return HttpResponseRedirect('/blog/get_article/%s' % article_id)
