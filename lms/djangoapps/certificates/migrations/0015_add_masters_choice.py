# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 15:14
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0014_change_eligible_certs_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatetemplate',
            name='mode',
            field=models.CharField(blank=True, choices=[(b'verified', b'verified'), (b'honor', b'honor'), (b'audit', b'audit'), (b'professional', b'professional'), (b'no-id-professional', b'no-id-professional'), (b'masters', b'masters')], default=b'honor', help_text='The course mode for this template.', max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='generatedcertificate',
            name='mode',
            field=models.CharField(choices=[(b'verified', b'verified'), (b'honor', b'honor'), (b'audit', b'audit'), (b'professional', b'professional'), (b'no-id-professional', b'no-id-professional'), (b'masters', b'masters')], default=b'honor', max_length=32),
        ),
    ]
