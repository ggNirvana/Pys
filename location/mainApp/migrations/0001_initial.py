# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mainInf',
            fields=[
                ('longi', models.CharField(max_length=20)),
                ('lati', models.CharField(max_length=20)),
                ('username', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
