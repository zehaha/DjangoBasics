# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=20)),
                ('eventType', models.CharField(max_length=20)),
                ('approvalStatus', models.CharField(max_length=30)),
                ('approved_by', models.ForeignKey(related_name='events_approved_by', to='accounts.UserProfile')),
                ('created_by', models.ForeignKey(related_name='events_created_by', to='accounts.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomName', models.CharField(max_length=20)),
                ('roomType', models.CharField(max_length=20)),
                ('roomNumber', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.DateField()),
                ('event', models.ForeignKey(to='home.Events')),
            ],
            options={
                'verbose_name_plural': 'Schedules',
            },
            bases=(models.Model,),
        ),
    ]
