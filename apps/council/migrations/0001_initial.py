# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Data spotkania')),
                ('hour', models.DateTimeField(verbose_name='Godzina spotkania')),
                ('code', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
