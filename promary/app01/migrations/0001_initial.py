# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('menus', models.ForeignKey(blank=True, null=True, to='app01.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('competence', models.ManyToManyField(to='app01.Competence')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10, unique=True, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('role', models.ManyToManyField(blank=True, null=True, to='app01.Role')),
            ],
        ),
        migrations.AddField(
            model_name='competence',
            name='menus',
            field=models.ForeignKey(blank=True, null=True, to='app01.Menu'),
        ),
    ]
