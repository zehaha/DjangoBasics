# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adminApproved', models.ForeignKey(related_name='requests_adminApproved', to='accounts.UserProfile')),
                ('chairApproves', models.ForeignKey(related_name='requests_chairApproves', to='accounts.UserProfile')),
                ('event', models.ForeignKey(to='home.Events')),
                ('requestedBy', models.ForeignKey(related_name='requests_requestedBy', to='accounts.UserProfile')),
                ('room', models.ForeignKey(to='home.Rooms')),
                ('schedule', models.ForeignKey(to='home.Schedules')),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
            bases=(models.Model,),
        ),
    ]
