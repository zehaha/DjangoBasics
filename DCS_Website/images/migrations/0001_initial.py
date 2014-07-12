# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'images_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.TextField')()),
            ('shown_in', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'images', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'images_image')


    models = {
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'shown_in': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['images']