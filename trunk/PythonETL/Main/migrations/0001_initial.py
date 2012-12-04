# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Template'
        db.create_table('Main_template', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('Main', ['Template'])

        # Adding model 'Job'
        db.create_table('Main_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Main.Template'])),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('dow', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('dom', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('hour', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('periodicity', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('Main', ['Job'])

        # Adding model 'Output'
        db.create_table('Main_output', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Main.Job'])),
            ('file', self.gf('django.db.models.fields.TextField')()),
            ('to_review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('Main', ['Output'])


    def backwards(self, orm):
        # Deleting model 'Template'
        db.delete_table('Main_template')

        # Deleting model 'Job'
        db.delete_table('Main_job')

        # Deleting model 'Output'
        db.delete_table('Main_output')


    models = {
        'Main.job': {
            'Meta': {'object_name': 'Job'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dom': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'dow': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'hour': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Main.Template']"}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'Main.output': {
            'Meta': {'object_name': 'Output'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Main.Job']"}),
            'to_review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'Main.template': {
            'Meta': {'object_name': 'Template'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Main']