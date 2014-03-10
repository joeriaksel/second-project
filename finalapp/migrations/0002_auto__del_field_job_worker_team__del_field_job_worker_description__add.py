# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Job.worker_team'
        db.delete_column(u'finalapp_job', 'worker_team')

        # Deleting field 'Job.worker_description'
        db.delete_column(u'finalapp_job', 'worker_description')

        # Adding field 'Job.worker_team_interaction'
        db.add_column(u'finalapp_job', 'worker_team_interaction',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Job.worker_notes'
        db.add_column(u'finalapp_job', 'worker_notes',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)

        # Adding field 'Job.employer_notes'
        db.add_column(u'finalapp_job', 'employer_notes',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


        # Changing field 'Job.employer_accurate_jobdescription'
        db.alter_column(u'finalapp_job', 'employer_accurate_jobdescription', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Job.worker_team'
        raise RuntimeError("Cannot reverse this migration. 'Job.worker_team' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Job.worker_team'
        db.add_column(u'finalapp_job', 'worker_team',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Job.worker_description'
        raise RuntimeError("Cannot reverse this migration. 'Job.worker_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Job.worker_description'
        db.add_column(u'finalapp_job', 'worker_description',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Deleting field 'Job.worker_team_interaction'
        db.delete_column(u'finalapp_job', 'worker_team_interaction')

        # Deleting field 'Job.worker_notes'
        db.delete_column(u'finalapp_job', 'worker_notes')

        # Deleting field 'Job.employer_notes'
        db.delete_column(u'finalapp_job', 'employer_notes')


        # Changing field 'Job.employer_accurate_jobdescription'
        db.alter_column(u'finalapp_job', 'employer_accurate_jobdescription', self.gf('django.db.models.fields.TextField')())

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
        u'finalapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'finalapp.employer': {
            'Meta': {'object_name': 'Employer'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'company_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'employer'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'finalapp.job': {
            'Meta': {'object_name': 'Job'},
            'date_changed_job': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created_job': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'employer_24hnotice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employer_accurate_jobdescription': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'employer_confirm_job_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employer_friendliness': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'employer_notes': ('django.db.models.fields.TextField', [], {}),
            'employer_punctual_payment': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'employer_responsiveness': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'employer_show': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.JobPost']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.Status']"}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.Worker']"}),
            'worker_24hnotice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'worker_friendliness': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_hours_worked': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_job_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'worker_language': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_notes': ('django.db.models.fields.TextField', [], {}),
            'worker_performance_quality': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_performance_speed': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_presentation': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_punctuality': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_responsiveness': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'worker_show': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'worker_team_interaction': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'finalapp.jobpost': {
            'Meta': {'object_name': 'JobPost'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.Category']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.Employer']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'hourly_rate': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'people_needed': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['finalapp.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'weekly_hours': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'workers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['finalapp.Worker']", 'through': u"orm['finalapp.Job']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'finalapp.mainuser': {
            'Meta': {'object_name': 'MainUser', '_ormbases': [u'auth.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'finalapp.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'finalapp.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'finalapp.worker': {
            'Meta': {'object_name': 'Worker'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'worker'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['finalapp']