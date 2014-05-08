import os
from datetime import datetime

def populate():
	add_user(email = '', username = 'admin', password = 'admin', group = 'Admin')
	add_user(email = '', username = 'faculty', password = 'faculty', group = 'Faculty')
	add_user(email = '', username = 'student', password = 'student', group = 'Students')
	print ('Added users and groups.')

	add_announcement(pub_date = datetime.now(), title = 'Sample Announcement 1',
	body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla orci libero, bibendum ac consequat eu, dignissim a urna.')
	add_announcement(pub_date = datetime.now(), title = 'Sample Announcement 2',
	body = 'Fusce sed dui sed mi sollicitudin porta porta nec purus. Proin vulputate dui turpis, in fermentum diam lacinia eu.')
	add_announcement(pub_date = datetime.now(), title = 'Sample Announcement 3',
	body = 'Proin eu dolor semper, elementum urna in, porttitor turpis. Vivamus et nisl in dolor accumsan pretium vel quis diam.')
	print ('Added announcements.')

	add_news(pub_date = datetime.now(), title = 'Sample News Article 1',
	body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla orci libero, bibendum ac consequat eu, dignissim a urna.')
	add_news(pub_date = datetime.now(), title = 'Sample News Article 2',
	body = 'Fusce sed dui sed mi sollicitudin porta porta nec purus. Proin vulputate dui turpis, in fermentum diam lacinia eu.')
	add_news(pub_date = datetime.now(), title = 'Sample News Article 3',
	body = 'Proin eu dolor semper, elementum urna in, porttitor turpis. Vivamus et nisl in dolor accumsan pretium vel quis diam.')
	print ('Added news articles.')

	add_event(date = datetime.now(), description = 'Sample Event 1')
	add_event(date = datetime.now(), description = 'Sample Event 2')
	add_event(date = datetime.now(), description = 'Sample Event 3')
	print ('Added events.')

	add_image(image = '/media/images/Autumn_Leaves.jpg', caption = 'Autumn Leaves', shown_in = 'b')
	add_image(image = '/media/images/Garden.jpg', caption = 'Garden', shown_in = 'c')
	add_image(image = '/media/images/Humpback_Whale.jpg', caption = 'Humpback Whale', shown_in = 'b')
	add_image(image = '/media/images/Oryx_Antelope.jpg', caption = 'Oryx Antelope', shown_in = 'c')
	add_image(image = '/media/images/Tree.jpg', caption = 'Tree', shown_in = 'b')
	add_image(image = '/media/images/Waterfall.jpg', caption = 'Waterfall', shown_in = 'c')
	print ('Added images.')

def add_user(email, username, password, group):
	u  =  User.objects.create_user(email = email, username = username, password = password)
	u.is_staff = True
	u.is_active = True
	g = Group.objects.create(name = group)
	g.user_set.add(u)
	g.save()
	u.save()
	return u

def add_announcement(pub_date, title, body):
	a  =  Announcement.objects.get_or_create(pub_date = pub_date, title = title, body = body)[0]
	return a

def add_event(date, description):
	e  =  Event.objects.get_or_create(date = date, description = description)[0]
	return e

def add_news(pub_date, title, body):
	n  =  NewsArticle.objects.get_or_create(pub_date = pub_date, title = title, body = body)[0]
	return n

def add_image(image, caption, shown_in):
	i  =  Image.objects.get_or_create(image = image, caption = caption, shown_in = shown_in)[0]
	return i

if __name__ == '__main__':
	print ("Starting DCS_Website population script...")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DCS_Website.settings')
	from django.contrib.auth.models import User, Group
	from announcements.models import Announcement
	from events.models import Event
	from images.models import Image
	from news.models import NewsArticle
	populate()
	print ('Population completed.')