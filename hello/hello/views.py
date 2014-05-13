from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from blog.models import Article


def home(request):
	return render_to_response('home.html', { 'articles' : Article.objects.all().order_by('-pub_date')[:5]})
