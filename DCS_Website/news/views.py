from django.shortcuts import render
from news.models import NewsArticle

# Create your views here.
def news_details(request, pk):
	"""Fetch the requested object with the given primary key from the database,
	create context by assigning the object to a corresponding variable in the template,
	and render the page using the context and the template in the given directory.
	"""
	news_article = NewsArticle.objects.get(id=pk)
	context = {'news_article' : news_article}
	return render(request, 'news/news.html', context)