# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userType', models.CharField(default=b'SA', max_length=2, choices=[(b'O', b'Organization'), (b'F', b'Faculty'), (b'G', b'Guest'), (b'SA', b'System Admin'), (b'BA', b'Building Admin'), (b'DC', b'Dept Chair')])),
                ('priorityLevel', models.IntegerField(default=0)),
                ('additionalProperties', models.TextField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
