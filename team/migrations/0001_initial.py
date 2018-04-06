# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=120, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('signup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='team.SignUp')),
                ('ref_id', models.CharField(default=b'ABC', max_length=150)),
                ('ip_address', models.CharField(default=b'ABC', max_length=120)),
            ],
            bases=('team.signup',),
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('join_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='team.Join')),
                ('ph', models.CharField(max_length=120)),
            ],
            bases=('team.join',),
        ),
    ]
