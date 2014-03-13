# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainUser'
        db.create_table(u'finalapp_mainuser', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'finalapp', ['MainUser'])

        # Adding model 'Employer'
        db.create_table(u'finalapp_employer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_number', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latitude', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('profile_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='employer', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'finalapp', ['Employer'])

        # Adding model 'Worker'
        db.create_table(u'finalapp_worker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_number', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latitude', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('profile_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='worker', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'finalapp', ['Worker'])

        # Adding model 'Category'
        db.create_table(u'finalapp_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'finalapp', ['Category'])

        # Adding model 'Tag'
        db.create_table(u'finalapp_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'finalapp', ['Tag'])

        # Adding model 'JobPost'
        db.create_table(u'finalapp_jobpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finalapp.Category'])),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finalapp.Employer'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('hourly_rate', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('weekly_hours', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latitude', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('longitude', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('people_needed', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('requirements', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'finalapp', ['JobPost'])

        # Adding M2M table for field tag on 'JobPost'
        m2m_table_name = db.shorten_name(u'finalapp_jobpost_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('jobpost', models.ForeignKey(orm[u'finalapp.jobpost'], null=False)),
            ('tag', models.ForeignKey(orm[u'finalapp.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['jobpost_id', 'tag_id'])

        # Adding model 'Status'
        db.create_table(u'finalapp_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'finalapp', ['Status'])

        # Adding model 'Job'
        db.create_table(u'finalapp_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finalapp.Status'])),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finalapp.Worker'])),
            ('job_post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finalapp.JobPost'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'finalapp', ['Job'])

        # Adding model 'WorkerReview'
        db.create_table(u'finalapp_workerreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['finalapp.Job'], unique=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('worker_show', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('worker_24hnotice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('worker_job_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('worker_hours_worked', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_responsiveness', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_performance_quality', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_performance_speed', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_punctuality', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_language', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_friendliness', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_team_interaction', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_presentation', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('worker_notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'finalapp', ['WorkerReview'])

        # Adding model 'EmployerReview'
        db.create_table(u'finalapp_employerreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['finalapp.Job'], unique=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('employer_show', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('employer_24hnotice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('employer_confirm_job_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('employer_responsiveness', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('employer_friendliness', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('employer_accurate_jobdescription', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('employer_punctual_payment', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('employer_notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'finalapp', ['EmployerReview'])


    def backwards(self, orm):
        # Deleting model 'MainUser'
        db.delete_table(u'finalapp_mainuser')

        # Deleting model 'Employer'
        db.delete_table(u'finalapp_employer')

        # Deleting model 'Worker'
        db.delete_table(u'finalapp_worker')

        # Deleting model 'Category'
        db.delete_table(u'finalapp_category')

        # Deleting model 'Tag'
        db.delete_table(u'finalapp_tag')

        # Deleting model 'JobPost'
        db.delete_table(u'finalapp_jobpost')

        # Removing M2M table for field tag on 'JobPost'
        db.delete_table(db.shorten_name(u'finalapp_jobpost_tag'))

        # Deleting model 'Status'
        db.delete_table(u'finalapp_status')

        # Deleting model 'Job'
        db.delete_table(u'finalapp_job')

        # Deleting model 'WorkerReview'
        db.delete_table(u'finalapp_workerreview')

        # Deleting model 'EmployerReview'
        db.delete_table(u'finalapp_employerreview')


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
            'latitude': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'employer'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'finalapp.employerreview': {
            'Meta': {'object_name': 'EmployerReview'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'employer_24hnotice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employer_accurate_jobdescription': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'employer_confirm_job_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employer_friendliness': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'employer_notes': ('django.db.models.fields.TextField', [], {}),
            'employer_punctual_payment': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'employer_responsiveness': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'employer_show': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['finalapp.Job']", 'unique': 'True'})
        },
        u'finalapp.job': {
            'Meta': {'object_name': 'Job'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.JobPost']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.Status']"}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finalapp.Worker']"})
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
            'latitude': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'longitude': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
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
            'latitude': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'worker'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'finalapp.workerreview': {
            'Meta': {'object_name': 'WorkerReview'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['finalapp.Job']", 'unique': 'True'}),
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
        }
    }

    complete_apps = ['finalapp']