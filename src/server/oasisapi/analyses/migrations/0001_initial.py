# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis_models', '0001_initial'),
        ('files', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('NOT_RAN', 'Not ran'), ('PENDING', 'Pending'), ('STARTED', 'Started'), ('STOPPED_COMPLETED', 'Stopped - Completed'), ('STOPPED_CANCELLED', 'Stopped - Cancelled'), ('STOPPED_ERROR', 'Stopped - Error')], default='NOT_RAN', editable=False, max_length=17)),
                ('task_id', models.CharField(blank=True, default='', editable=False, max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to=settings.AUTH_USER_MODEL)),
                ('input_errors_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input_errors_file_analyses', to='files.RelatedFile')),
                ('input_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input_file_analyses', to='files.RelatedFile')),
                ('model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='analyses', to='analysis_models.AnalysisModel')),
                ('output_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output_file_analyses', to='files.RelatedFile')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to='portfolios.Portfolio')),
                ('settings_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings_file_analyses', to='files.RelatedFile')),
            ],
            options={
                'verbose_name_plural': 'analyses',
            },
        ),
    ]
