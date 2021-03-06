# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.bank_account'
        db.alter_column(u'rollpay_userprofile', 'bank_account', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    def backwards(self, orm):

        # Changing field 'UserProfile.bank_account'
        db.alter_column(u'rollpay_userprofile', 'bank_account', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rollpay.merchant': {
            'Meta': {'object_name': 'Merchant'},
            'affiliate_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'total_orders': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '30'})
        },
        u'rollpay.order': {
            'Meta': {'object_name': 'Order'},
            'ammount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'cashback': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rollpay.Merchant']"}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'}),
            'track_link': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'verification': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rollpay.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': [u'auth.User']},
            'bank_account': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'bank_ifsc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'orders': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rollpay.Order']", 'symmetrical': 'False'}),
            'payee': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tax_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['rollpay']