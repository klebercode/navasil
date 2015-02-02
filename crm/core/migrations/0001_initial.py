# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # # Adding model 'Customer'
        # db.create_table(u'core_customer', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        #     ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        #     ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        #     ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        #     ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        #     ('district', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('complement', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        #     ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        #     ('city', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        #     ('observation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        # ))
        # db.send_create_signal(u'core', ['Customer'])

        # # Adding model 'People'
        # db.create_table(u'core_people', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        #     ('cpf', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
        #     ('rg', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        #     ('expeditor', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        #     ('expeditor_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        #     ('brith_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        #     ('sex', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        #     ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        #     ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        #     ('district', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('complement', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        #     ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        #     ('city', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        #     ('job', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        #     ('capacity', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        #     ('registration', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        #     ('ord_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        #     ('observation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        #     ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Customer'])),
        # ))
        # db.send_create_signal(u'core', ['People'])

        # # Adding model 'ContactPhone'
        # db.create_table(u'core_contactphone', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        #     ('operate', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        #     ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Customer'])),
        #     ('people', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.People'])),
        # ))
        # db.send_create_signal(u'core', ['ContactPhone'])

        # # Adding model 'ContactEmail'
        # db.create_table(u'core_contactemail', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        #     ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Customer'])),
        #     ('people', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.People'])),
        # ))
        # db.send_create_signal(u'core', ['ContactEmail'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'core_customer')

        # Deleting model 'People'
        db.delete_table(u'core_people')

        # Deleting model 'ContactPhone'
        db.delete_table(u'core_contactphone')

        # Deleting model 'ContactEmail'
        db.delete_table(u'core_contactemail')


    models = {
        u'core.contactemail': {
            'Meta': {'ordering': "['email']", 'object_name': 'ContactEmail'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Customer']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'people': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.People']"})
        },
        u'core.contactphone': {
            'Meta': {'ordering': "['number']", 'object_name': 'ContactPhone'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'operate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.People']"}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.customer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'core.people': {
            'Meta': {'ordering': "['name']", 'object_name': 'People'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'brith_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Customer']"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'expeditor': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'expeditor_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ord_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'registration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
