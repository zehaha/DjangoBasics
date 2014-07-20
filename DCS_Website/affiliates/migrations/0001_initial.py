# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Affiliate'
        db.create_table(u'affiliates_affiliate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
            ('corporate_donor', self.gf('django.db.models.fields.BooleanField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contribution', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'affiliates', ['Affiliate'])


    def backwards(self, orm):
        # Deleting model 'Affiliate'
        db.delete_table(u'affiliates_affiliate')


    models = {
        u'affiliates.affiliate': {
            'Meta': {'object_name': 'Affiliate'},
            'contribution': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'corporate_donor': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'status': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['affiliates']