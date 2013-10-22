# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.position'
        db.add_column('social_media_links_link', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Link.position'
        db.delete_column('social_media_links_link', 'position')


    models = {
        'social_media_links.link': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social_media_links.LinkType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
