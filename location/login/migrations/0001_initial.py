# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInf',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('isOnline', models.BooleanField(default=False)),
            ],
        ),
    ]
