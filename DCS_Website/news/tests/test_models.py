from django.template.loader import render_to_string
from django.test import TestCase, Client
from news.models import NewsArticle
from django.conf.urls import patterns, url

class NewsModelTest(TestCase):
	"""Test for News models"""
	def create_news(self,pub_date='2014-04-30',title='asdasd',body='asdasd'):
		return NewsArticle.objects.create(pub_date=pub_date,title=title,body=body)
	def test_news_creation(self):
		news = self.create_news()
		self.assertTrue(isinstance(news,NewsArticle))
		self.assertEqual(news.__str__(),(news.title))
