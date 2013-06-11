# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkType'
        db.create_table('social_media_links_linktype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('social_media_links', ['LinkType'])

        # Adding model 'Link'
        db.create_table('social_media_links_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social_media_links.LinkType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
        ))
        db.send_create_signal('social_media_links', ['Link'])


    def backwards(self, orm):
        # Deleting model 'LinkType'
        db.delete_table('social_media_links_linktype')

        # Deleting model 'Link'
        db.delete_table('social_media_links_link')


    models = {
        'social_media_links.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social_media_links.LinkType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4000'})
        },
        'social_media_links.linktype': {
            'Meta': {'object_name': 'LinkType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['social_media_links']
