# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Faculty'
        db.create_table(u'people_faculty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('consultation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('research', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['Faculty'])

        # Adding model 'Student'
        db.create_table(u'people_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('org_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'people', ['Student'])

        # Adding model 'Staff'
        db.create_table(u'people_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'people', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Faculty'
        db.delete_table(u'people_faculty')

        # Deleting model 'Student'
        db.delete_table(u'people_student')

        # Deleting model 'Staff'
        db.delete_table(u'people_staff')


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
        u'people.staff': {
            'Meta': {'object_name': 'Staff'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.student': {
            'Meta': {'object_name': 'Student'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['people']