# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lab'
        db.create_table(u'research_lab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('head', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'research', ['Lab'])

        # Adding model 'Field'
        db.create_table(u'research_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lab_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Lab'])),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'research', ['Field'])

        # Adding model 'Adviser'
        db.create_table(u'research_adviser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lab_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Lab'])),
            ('adviser_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Faculty'])),
        ))
        db.send_create_signal(u'research', ['Adviser'])


    def backwards(self, orm):
        # Deleting model 'Lab'
        db.delete_table(u'research_lab')

        # Deleting model 'Field'
        db.delete_table(u'research_field')

        # Deleting model 'Adviser'
        db.delete_table(u'research_adviser')


    models = {
        u'people.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'consultation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'research.adviser': {
            'Meta': {'object_name': 'Adviser'},
            'adviser_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Faculty']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Lab']"})
        },
        u'research.field': {
            'Meta': {'object_name': 'Field'},
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Lab']"})
        },
        u'research.lab': {
            'Meta': {'object_name': 'Lab'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'head': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['research']