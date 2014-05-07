DCS-Website
===========

Django-based website for the Department of Computer Science in the University of the Philippines.

Everything's in the tutorial :bd  
https://docs.djangoproject.com/en/1.6/intro/tutorial01/

Once you've pulled the files, open the command prompt, go to the directory where you've placed the files (cd .../DCS_Website) and enter "manage.py runserver".  
Using your browser, go to http://127.0.0.1:8000 to view the homepage. You can now view the latest three announcements, events, and news articles.
The admin page (http://127.0.0.1:8000/admin) can be accessed through all of the accounts: superadmin, admin, faculty, and student. Their passwords are the same as the usernames. They have different permissions based on the group they are in. The admin capability of approving changes made by student accounts is yet to be added.

Templates for homepage, admin, and registration are in DCS_Website/templates.  
Templates for apps are in the respective templates folders in their directories.  
They're for the layout team, so that they know how to show the model variables.

You can now upload images! The image app is in the admin page. Just use the ImageField to upload a file. It will automatically be sent to the media folder, under images. I added some samples to the homepage. Look at the home template to see how to serve images from the media folder.  
IMPORTANT NOTE: For the image app to work, you need to install a Python program called Pillow, a Python Imaging Library fork. Just open the command prompt and enter "pip install pillow", like what you did with Django.

Integrated layout with back-end! See DCS_Website/views.py and templates/home/home.html to see how to fetch data from the database. Static files like non-user-uploaded images, stylesheets, etc. can be found in images/static because for some reason, the django staticfiles app can't find them if they aren't in another app folder. Might be fixed in a later update.
