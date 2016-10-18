# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0004_auto_20161010_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='meeting',
            field=models.ForeignKey(default=1, verbose_name='Spotkanie', to='council.Meeting'),
            preserve_default=False,
        ),
    ]
